
import tensorflow as tf
import numpy as np
from os import sys


def pixel_locator(p, n, f ):
    '''
    p: point cloud, n: center of photo, f: focal point
    return location of the point cloud on the photo
    '''
    point_num = len(p)
    p = tf.Variable(p[:,0:3], tf.float32)
    n = tf.Variable(n, tf.float32)
    f = tf.Variable(f, tf.float32)

    v = tf.subtract(f, n) # normal vector of the photo
    lv = tf.subtract(f, p) # line vector
    
    vpt = tf.multiply(v, lv)
    
    if(vpt == 0):
        print("the line is parallel with the photo")
        return None
    else:
        # for any point r(x,y,z) on the photo
        t = tf.divide(tf.multiply(v, tf.subtract(n, p)), vpt)
        return tf.add(p, tf.multiply(lv, t))
data = np.loadtxt(sys.argv[1], delimiter = " ")

print("max x: %f max y: %f max z: %f" % (max(data[:,0]),max(data[:,1]), max(data[:,2])))
print("min x: %f min y: %f min z: %f" % (min(data[:,0]),min(data[:,1]), min(data[:,2])))

photo_center = np.array(max(data[:,0]),max(data[:,1]), max(data[:,2])*1.3)
focal_point = np.array(max(data[:,0]),max(data[:,1]), max(data[:,2])*1.5)


print(data.shape)
data = pixel_locator(data, photo_center, focal_point)
print(data.shape)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    data = sess.run(data) # any data returned by sess.run is numpy.array
    print(data.shape)
    np.savetxt(sys.argv[2], data, fmt = "%.3f %.3f %.3f")

