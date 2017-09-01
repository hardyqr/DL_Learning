import numpy as np
import tensorflow as tf
import sys
import time
import cv2

def calc_func(f, p, v, x):
    '''
    f: focal distance, 
    p: position of the camera, 
    v: direction of the camera(from center of camera to focal point)
    x: point cloud
    '''
    return f * v - f * f * (p + f * v - x) / (1 + np.sum((p - x) * v) / f)

def timeit(func, *args, **kwargs):
    s = time.time()
    func(*args, **kwargs)
    e = time.time()
    print("USE <\033[1;32m%.2f\033[0m> s"%(e - s))

def calc(data, f, p, v):
    data[:, :3] = np.apply_along_axis(calc_func(f, p, v), 1, data[:, :3])

def gen_photo(data, a, b, v, o):
    photo = np.zeros([a, b, 3])
    xs = np.sum(data[:, :3] * o, axis=1)
    ys = np.sum(data[:, :3] * np.cross(o, v), axis=1)
    xs = (a - 1) * (xs - xs.min()) / (xs.max() - xs.min())
    ys = (b - 1) * (ys - ys.min()) / (ys.max() - ys.min())
    for i, (x,y) in enumerate(zip(xs, ys)):
        photo[int(x), int(y), :] = data[i, 3:6]
        # print(photo[int(x), int(y), :])
    return photo

def main(ifn, ofn, f, p, v, o):
    data = np.loadtxt(ifn)

    print("data stat")
    print("x max: ", max(data[:,0]), "min x:", min(data[:,0]))
    print("y max: ", max(data[:,1]), "min y:", min(data[:,1]))
    print("z max: ", max(data[:,2]), "min z:", min(data[:,2]))

    timeit(calc, data, f, p, v)
    #print(np.min(data, axis=1))
    #print(np.max(data, axis=1))
    photo = gen_photo(data, 400, 400, v, o)
    #print(photo)
    cv2.imwrite(ofn+".jpg", photo)
    # np.savetxt(ofn, data, fmt="%.4f")

if __name__ == "__main__":
    def str2vec(s):
        return np.array(list(map(float, s.strip().split(","))))
    args = sys.argv[1:3] + [float(sys.argv[3])] + [str2vec(x) for x in sys.argv[4:]]
    timeit(main, *args)
