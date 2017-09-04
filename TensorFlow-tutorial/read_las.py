# Freddy @BNU 387
# Sep 4, 2017

import laspy
import numpy as np
import sys


def read_las(address):
    # Open a file in read mode:
    inFile = laspy.file.File(address)
    
    # Grab a numpy dataset of our clustering dimensions:
    dataset = np.vstack([inFile.X, inFile.Y, inFile.Z]).transpose()
    print(dataset.shape)
    return dataset


'''
# Find the nearest 5 neighbors of point 100.

neighbors = flann.nn(dataset, dataset[100,], num_neighbors = 5)
print("Five nearest neighbors of point 100: ")
print(neighbors[0])
print("Distances: ")
print(neighbors[1])
'''
