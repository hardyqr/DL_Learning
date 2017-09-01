# Freddy @Terminal 1, Capital Airport, Beijing
# Sep 2, 2017
import tensorflow as tf
import numpy as np
from os import sys
import time
import cv2

'''
def pixel_locator():
    
    #p: point cloud, n: center of photo, f: focal point
    #return location of the point cloud on the photo
    
    p = tf.placeholder(tf.float32,[None,3])
    n = tf.placeholder(tf.float32,[None,3])
    f = tf.placeholder(tf.float32,[None,3])
    v = tf.subtract(f, n) # normal vector of the photo
    lv = tf.subtract(f, p) # line vector

    vpt = tf.reduce_sum(tf.multiply(v, lv), 1)
    
    if(vpt == 0):
        print("the line is parallel with the photo")
        return None
    else:
        # for any point r(x,y,z) on the photo
        t = tf.divide(tf.reduce_sum(tf.multiply(v, tf.subtract(n, p)), 1), vpt)

        return tf.add(p, tf.multiply(lv,t[0])), p,n,f
'''

def pixel_locator():
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


def parameter_setting():
    photo_center = np.array([max(original_data[:,0])*1.2,max(original_data[:,1])*1.2, max(original_data[:,2])*1.3])
    focal_dir = np.array( [0 , 0 , max(original_data[:,2])*1.5 ] )
    focal_distance = (max(original_data[:,2]) - min(original_data[:,2]))*0.3
    return photo_center, focal_dir, focal_distance

def main():
    original_data = data_loader(sys.argv[1])
    data,x,p,v,f = pixel_locator()

    photo_center, focal_dir, focal_distance = parameter_setting()
    
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
        #print(data)
        original_data[:,:3] = data
        #print(data.shape)
        np.savetxt(sys.argv[2], original_data, fmt = "%.3f %.3f %.3f %i %i %i %i")



if __name__ == "__main__":
    timeit(main,*args)
