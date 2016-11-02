import numpy as np
import os

def zoom(x,y,z,n):
    X=x*n
    Y=y*n
    Z=z*n
    return X,Y,Z

path='/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Stanford3dDataset_v1.1-5/Area_5/'
rooms=os.listdir(path)
for name in rooms:
    if 'office' in name:
        items=os.listdir(path+name+'/Annotations')
        for item in items:
            if 'table' in item:
                input_data=path+name+'/Annotations/'+item
                P = np.loadtxt(input_data, delimiter=' ', unpack=True)
                IX=P[0,:]
                IY=P[1,:]
                IZ=P[2,:]
                IR=P[3,:]
                IG=P[4,:]
                IB=P[5,:]
                #IL=P[6,:]
                print(IX,IY)
                length=len(list(IB))
                size_count=0
                while(size_count<10):
                    size=np.random.normal(loc=1,scale=0.5,size=None)
                    if 0.5<size<1.5:sizes.append(size)
                output_data=[]
                for size in sizes:
                    output_data.append('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/Area_5_table_zooms/'+name+'_'+item[:-4]+'_'+str(size)+'.txt')
                    XZ,YZ,ZZ = zoom(IX,IY,,IZ,size)
                    output=np.zeros(shape=(7,length))
                    output[0,:]=XZ
                    output[1,:]=YZ
                    output[2,:]=ZZ
                    output[3,:]=IR
                    output[4,:]=IG
                    output[5,:]=IB
                    output[6,:]=9
                    #output[6,:]=label
                    np.savetxt(item,output.transpose(),fmt='%.5f',delimiter=' ',newline='\n')
