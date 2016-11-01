import numpy as np
import os

def rotation(x,y,n):
    X=x*np.cos(n)+y*np.sin(n)
    Y=-x*np.sin(n)+y*np.cos(n)
    return X,Y


rooms=os.listdir('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Stanford3dDataset_v1.1-5/Area_5/')
for name in rooms:
    if 'office' in name:
        items=os.listdir('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Stanford3dDataset_v1.1-5/Area_5/'+name+'/Annotations')
        for item in items:
            if 'table' in item:
                input_data='/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Stanford3dDataset_v1.1-5/Area_5/'+name+'/Annotations/'+item
                P = np.loadtxt(input_data, delimiter=' ', unpack=True)
                IX=P[0,:]
                IY=P[1,:]
                IZ=P[2,:]
                IR=P[3,:]
                IG=P[4,:]
                IB=P[5,:]
                #IL=P[6,:]
                print(IX,IY)
                xs=[x*45 for x in range(8)]
                output_data=[]
                for x in xs:
                    output_data.append('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/Area_5_table_rotations/'+name+'_'+item[:-4]+'_'+str(x)+'.txt')
                count=0
                length=len(list(IB))
                for item in output_data:
                    angle = count*45
                    IXR,IYR = rotation(IX,IY,angle)
                    output=np.zeros(shape=(7,length))
                    output[0,:]=IXR
                    output[1,:]=IYR
                    output[2,:]=IZ
                    output[3,:]=IR
                    output[4,:]=IG
                    output[5,:]=IB
                    output[6,:]=9
                    #output[6,:]=label
                    np.savetxt(item,output.transpose(),fmt='%.5f',delimiter=' ',newline='\n')
                    count=count+1
