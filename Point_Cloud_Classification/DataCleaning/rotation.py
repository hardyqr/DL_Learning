import numpy as np
for i in range(1,9):
    input_data='/Users/Fangyu/Desktop/untitled folder/'+'table_'+str(i)+'.txt'
    P = np.loadtxt(input_data, delimiter=' ', unpack=True)
    IX=P[0,:]
    IY=P[1,:]
    IZ=P[2,:]
    IR=P[3,:]
    IG=P[4,:]
    IB=P[5,:]

    xs=[x*10 for x in range(36)]
    output_data=[]
    for x in xs:
        output_data.append('/Users/Fangyu/Desktop/untitled folder/rotations/'+'table_'+str(i)+'_'+str(x)+'.txt')
    def rotation(x,y,n):
        X=x*np.cos(n)+y*np.sin(n)
        Y=-x*np.sin(n)+y*np.cos(n)
        return X,Y
    length=len(IX)
    label=np.array([1]*length)

    count=0
    for item in output_data:
        angle = count*10
        IXR,IYR = rotation(IX,IY,angle)
        output=np.zeros(shape=(7,length))
        output[0,:]=IXR
        output[1,:]=IYR
        output[2,:]=IZ
        output[3,:]=IR
        output[4,:]=IG
        output[5,:]=IB
        output[6,:]=label
        np.savetxt(item,output.transpose(),fmt='%.5f',delimiter=' ',newline='\n')
        count=count+1
