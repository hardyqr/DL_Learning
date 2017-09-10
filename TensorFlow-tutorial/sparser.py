
import numpy as np
from read_las import read_las
import sys
import random
import laspy 


'''
sys.argv[1]: address of .las (input)
sys.argv[2]: X% of the original density
'''


def sparser(input_add = sys.argv[1], density = sys.argv[2], ouput_add) = sys.argv[3]:
    data = read_las(input_add)
    
    index = np.random.randint(0, high=100, size=data.shape[0], dtype='int64') < int(density)
    
    data = data[index]
    
    #print(index)
    #print(data.points)
    
    header = laspy.header.Header()
    outFile = laspy.file.File(output_add, mode = "w", header = header)
    
    outFile.X = data[:,0]
    outFile.Y = data[:,1]
    outFile.Z = data[:,2]
    
    outFile.close()
