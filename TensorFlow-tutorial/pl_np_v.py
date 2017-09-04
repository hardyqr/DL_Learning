import numpy as np
import tensorflow as tf
import sys
import time
import cv2
from read_las import read_las


def calc_func(f, p, v):
    return lambda x : f * v - f * f * (p + f * v - x) / (1 + np.sum((p - x) * v) / f)

def timeit(func, *args, **kwargs):
    s = time.time()
    func(*args, **kwargs)
    e = time.time()
    print("USE <\033[1;32m%.2f\033[0m> s"%(e - s))

def calc(data, f, p, v):
    data[:, :3] = np.apply_along_axis(calc_func(f, p, v), 1, data[:, :3])

def gen_photo(data, a, b, v, o):
    photo = np.zeros([a, b, 3])
    labels = np.zeros([a,b])
    xs = np.sum(data[:, :3] * o, axis=1)
    ys = np.sum(data[:, :3] * np.cross(o, v), axis=1)
    print(xs[1], xs[10], xs[100],xs[1000])
    xs = (a - 1) * (xs - xs.min()) / (xs.max() - xs.min())
    ys = (b - 1) * (ys - ys.min()) / (ys.max() - ys.min())
    for i, (x,y) in enumerate(zip(xs, ys)):
        photo[int(x), int(y), :] = data[i, 3:6]
        labels[int(x), int(y)] = data[i, 6]
        # print(photo[int(x), int(y), :])
    return photo, labels

def main(ifn, ofn, f, p, v, o):
    if "txt" in ifn:
        data = np.loadtxt(ifn).astype(np.float32)
    else:
        data = read_las(ifn).astype(np.float32)

    data[:,:3]*=1e-4
    print("data stat")
    print("x max: ", max(data[:,0]), "min x:", min(data[:,0]))
    print("y max: ", max(data[:,1]), "min y:", min(data[:,1]))
    print("z max: ", max(data[:,2]), "min z:", min(data[:,2]))
    print(data[:,6])
    print(np.sum(data[:,6]))

    timeit(calc, data, f, p, v)
    #print(np.min(data, axis=1))
    #print(np.max(data, axis=1))
    #np.savetxt("tmp.txt", data, fmt="%.3f")
    photo,labels = gen_photo(data, 448, 448, v, o)
    #print(photo)
    cv2.imwrite(ofn+".jpg", photo)
    print(labels[0],labels[300])
    #print(labels)
    print(labels.shape)
    np.savez(ofn+".npz", labels)
    # np.savetxt(ofn, data, fmt="%.4f")

if __name__ == "__main__":
    def str2vec(s):
        return np.array(list(map(float, s.strip().split(","))))
    args = sys.argv[1:3] + [float(sys.argv[3])] + [str2vec(x) for x in sys.argv[4:]]
    timeit(main, *args)
