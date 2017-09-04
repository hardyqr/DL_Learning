
import numpy as np
from read_las import read_las
import sys
import random
import laspy 

data = read_las(sys.argv[1])

index = np.random.randint(0, high=100, size=data.shape[0], dtype='int64') < int(sys.argv[2])

data = data[index]



print(index)
print(data.points)

header = laspy.header.Header()
outFile = laspy.file.File("./output.las", mode = "w", header = header)
outFile.X = data[:,0]
outFile.Y = data[:,1]
outFile.Z = data[:,2]

outFile.close()
