import numpy as np
def get_info_with_address(data_address):
    data= np.loadtxt(data_address, delimiter=' ', unpack=True)
    IX=data[0,:]
    IY=data[1,:]
    IZ=data[2,:]
    #IR=data[3,:]
    #IG=data[4,:]
    #IB=data[5,:]
    IL=data[6,:]
    IL_list=list(IL)
    point_num=len(IL_list)
    table_num=IL_list.count('9')
    chair_num=IL_list.count('5')
    x_max=max(IX)
    y_max=max(IY)
    z_max=max(IZ)
    x_min=min(IX)
    y_min=min(IY)
    z_min=min(IZ)
    x_mean=np.mean(IX)
    y_mean=np.mean(IY)
    z_mean=np.mean(IZ)
    #r=np.linalg.norm([x_max,y_max,z_max]-[x_min,y_min,z_min])/2
    return x_max,y_max,z_max,x_min,y_min,z_min,x_mean,y_mean,z_mean,point_num,table_num,chair_num

def get_info_with_data(data):
    #data=data.transpose()
    #IX=data[:,0]
    #IY=data[:,1]
    #IZ=data[:,2]
    #IR=data[3,:]
    #IG=data[4,:]
    #IB=data[5,:]
    #IL=data[:,6]
    #print(IL)
    #IL_list=list(IL)
    #table_num=IL_list.count('9')
    #chair_num=IL_list.count('5')
    data_item=data[data[:,6]==9]
    item_X=data_item[:,0]
    item_Y=data_item[:,1]
    item_Z=data_item[:,2]
    x_max=max(item_X)
    y_max=max(item_Y)
    z_max=max(item_Z)
    x_min=min(item_X)
    y_min=min(item_Y)
    z_min=min(item_Z)
    table_num_in=len(list(item_Z))
    #x_mean=np.mean(IX)
    #y_mean=np.mean(IY)
    #z_mean=np.mean(IZ)
    #r=np.linalg.norm((x_max,y_max,z_max)-(x_min,y_min,z_min))/2
    return x_max,y_max,z_max,x_min,y_min,z_min,table_num_in


def get_item_info(data_address):
    data= np.loadtxt(data_address, delimiter=' ', unpack=True)
    IX=data[0,:]
    IY=data[1,:]
    IZ=data[2,:]
    #IR=data[3,:]
    #IG=data[4,:]
    #IB=data[5,:]
    #IL=data[6,:]
    #IL_list=list(IL)
    #point_num=len(IL_list)
    #table_num=IL_list.count('9')
    #chair_num=IL_list.count('5')
    IZ_list=list(IZ)
    point_num=len(IZ_list)
    x_max=max(IX)
    y_max=max(IY)
    z_max=max(IZ)
    x_min=min(IX)
    y_min=min(IY)
    z_min=min(IZ)
    x_mean=np.mean(IX)
    y_mean=np.mean(IY)
    z_mean=np.mean(IZ)
    #r=np.linalg.norm([x_max,y_max,z_max]-[x_min,y_min,z_min])/2
    return x_max,y_max,z_max,x_min,y_min,z_min,x_mean,y_mean,z_mean,point_num

'''
            clutter:0
            beam:1
            board:2
            bookcas:3
            ceiling:4
            chair:5
            column:6
            door:7
            floor:8
            table:9
            wall:10
            window:11
Details can be found in read_all_stanford.py
'''
