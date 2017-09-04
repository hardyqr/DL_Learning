# Freddy @Terminal 1, Capital Airport, Beijing
# Sep 2, 2017
import tensorflow as tf
import numpy as np
from os import sys
import time
import cv2
from read_las import read_las

np.seterr(divide='ignore', invalid='ignore')

def pixel_locator():
    '''
    f: focal distance, 
    p: position of the camera, 
    v: direction of the camera(from center of camera to focal point)
    x: point cloud
    '''
    x = tf.placeholder(tf.float32,[None,3])
    p = tf.placeholder(tf.float32,[None,3])
    v = tf.placeholder(tf.float32,[None,3])
    f = tf.placeholder(tf.float32,[None,1])
    divider = tf.reduce_sum( (p - x) * v , axis=0, keep_dims=True) + 1 
    result = f * v - f * f * f * (p + f * v - x) / divider

    return result, x, p, v,f


def timeit(func, *args, **kwargs):
    s = time.time()
    func(*args, **kwargs)
    e = time.time()
    print("USE <\033[1;32m%.2f\033[0m> s" % (e - s))

def data_loader(address):
    print("load data...")
    original_data = np.loadtxt(address)
    print("load complete")
    print("------data stats------")
    print("max x: %f max y: %f max z: %f" % (max(original_data[:,0]),max(original_data[:,1]), max(original_data[:,2])))
    print("min x: %f min y: %f min z: %f" % (min(original_data[:,0]),min(original_data[:,1]), min(original_data[:,2])))
    return original_data


def parameter_setting(original_data):
    photo_center = np.array([max(original_data[:,0])*1.2,max(original_data[:,1])*1.2, max(original_data[:,2])*20])
    focal_dir = np.array( [0 , 0 , max(original_data[:,2])*1.5 ] )
    focal_distance = (max(original_data[:,1]) - min(original_data[:,1]))*0.5
    return photo_center, focal_dir, focal_distance

def generate_photo(data, a, b, v, o):
    print(data[0],data[1],data[3], data[100],data[1000])
    photo = np.zeros([a, b, 3])
    xs = np.sum(data[:, :3] * o, axis=1)
    ys = np.sum(data[:, :3] * np.cross(o, v), axis=1)

    print(xs[0],xs[1],xs[3],xs[100],xs[1000])
    print("xs.max: ", xs.max)
    print("ys.max: ", ys.max)
    xs = (a - 1) * (xs - xs.min()) / (xs.max() - xs.min())
    ys = (b - 1) * (ys - ys.min()) / (ys.max() - ys.min())

    for i, (x,y) in enumerate(zip(xs, ys)):
        try:
            photo[int(x), int(y), :] = data[i, 3:6]
            # print(photo[int(x), int(y), :])
            print("success")
        except:
            continue
        
    return photo
'''
def generate_photo(data, a, b, v, o):
    photo = np.zeros([a, b, 3])
    print(data[:,:3].shape)

    print(o.shape)
    #print(v.shape)

    yd = np.cross(o,v)
    print(yd)
    print(yd.shape)
    xs = np.sum(data[:, :3] * o, axis=0)
    ys = np.sum(data[:, :3] * yd, axis=0)

    print(xs[0],xs[1],xs[2])
    print("xs.shape:", xs.shape)
    xs = (a - 1) * (xs - xs.min()) / (xs.max() - xs.min())
    ys = (b - 1) * (ys - ys.min()) / (ys.max() - ys.min())
    print("-----point 1-----")
    print(xs[0],xs[1],xs[2])
    for i, (x,y) in enumerate(zip(xs, ys)):
        photo[int(x), int(y), :] = data[i, 3:6]
        # print(photo[int(x), int(y), :])
    return photo


def generate_photo(data, a, b, v, o):
    #data:
    #a: length
    #b: width
    #v: direction of the camera(from center of camera to focal point)
    #o: positive direction of the photo
    #data = data.eval
    #v = v.eval
    #o = o.eval
    #photo = np.zeros([a, b, 3])
    photo = np.zeros([a, b, 3])
    #xs = np.sum(data[:, :3] * o, axis=1)
    xs = np.sum(data[:, :3] * o, axis=0)
    #print("xs.shape:", xs.shape)

    #ys = np.sum(data[:, :3] * np.cross(o, v), axis=1)
    ys = np.sum(data[:, :3] * np.cross(o, v), axis=0)
    #ys = (b - 1) * (ys - ys.min()) / (ys.max() - ys.min())
    #xs = (a - 1) * (xs - xs.min()) / (xs.max() - xs.min())

    print("xs.shape:", xs.shape)
    #photo = []
    for i in range(xs.shape[0]):
        #x_ = int(xs[i])
        #y_ = int(ys[i])
        #x_ = int(str(''.join(xs[i])))
        #y_ = int(str(''.join(ys[i])))
        photo[xs[i], ys[i], :] = data[i, 3:6]
        # print(photo[int(x), int(y), :])
    return photo
'''
#def str2vec(s):

def main():
    if "txt" in sys.argv[1]:
        original_data = data_loader(sys.argv[1])
    else:
        original_data = read_las(sys.argv[1])

    data,x,p,v,f = pixel_locator()

    photo_center, focal_dir, focal_distance = parameter_setting(original_data)
    
    init = tf.global_variables_initializer()
    
    with tf.Session() as sess:
        sess.run(init)
        point_num = len(original_data)
        photo_center = np.transpose(np.reshape(np.repeat(photo_center,point_num),(3,point_num)))
        focal_dir = np.transpose(np.reshape(np.repeat(focal_dir,point_num),(3,point_num)))
        focal_distance = np.transpose(np.reshape(np.repeat(focal_distance,point_num),(1,point_num)))
        
        print("photo_center.shape:", photo_center.shape)
        print("focal_dir.shape: ",focal_dir.shape)
        print("focal_distance.shape: ",focal_distance.shape)
        
        print("to run...")
        
        data = sess.run(data,feed_dict={
            x: original_data[:,:3] ,
            p: photo_center ,
            v: focal_dir,
            f: focal_distance }) # any data returned by sess.run is numpy.array
        print("max x: %f max y: %f max z: %f" % (max(original_data[:,0]),max(original_data[:,1]), max(original_data[:,2])))
        print(max(data[:,0]), max(data[:,1]),max(data[:,2]))
        print(data[0],data[10],data[100])
        original_data[:,:3] = data


        #print(data.shape)
        #np.savetxt(sys.argv[2], original_data, fmt = "%.3f %.3f %.3f %i %i %i %i")
        #original_data = original_data.eval
            
        o = np.array([1,0,0])
        #v = v.eval
        #v = v[0].eval
        #print("v:", v)
        #print("o:", o)
        photo = generate_photo(original_data, 400,400,focal_dir,o)
        #print(photo.shape)
        print(photo)
        print(photo[0])
        cv2.imwrite("test.jpg", photo)


if __name__ == "__main__":
    #timeit(main,*args)
    main()
