import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import Birch
from sklearn.cluster import KMeans
import os
from get_info import *

def get_list_matrix(data_address,  xyz_range):
    data= np.loadtxt(data_address, delimiter=' ', unpack=True)
    X = data.transpose()
    hx,hy,hz,lx,ly,lz = xyz_range
    X = X[
      (X[:,0]>=lx)&
      (X[:,0]<hx)&
      (X[:,1]>=ly)&
      (X[:,1]<hy)&
      (X[:,2]>=lz)&
      (X[:,2]<hz)
    ]
    return X

def Build_and_Evaluate_Eye_Window(table_address,scene_address):
    x_max,y_max,z_max,x_min,y_min,z_min,x_mean,y_mean,z_mean,point_num=get_item_info(table_address)
    E_x=np.random.normal(loc=x_mean, scale=1.0, size=None)#loc 均值，scale 标准差，size大小。
    E_y=np.random.normal(loc=y_mean, scale=1.0, size=None)#loc 均值，scale 标准差，size大小。
    E_z=np.random.normal(loc=z_mean, scale=1.0, size=None)#loc 均值，scale 标准差，size大小。
    h=abs(z_max-z_min)
    l=E_l=abs(np.random.normal(loc=max(abs(x_max-x_min),abs(y_max-y_min),abs(z_max-z_min)), scale=3.0, size=None))#loc 均值，scale 标准差，size大小。
    print(x_mean,y_mean,z_mean)
    print(E_x,E_y,E_z,l,E_l)
    print(E_x+l/2,E_y+l/2,E_z+l/2,E_x-l/2,E_y-l/2,E_z-l/2)
    Eye_Window=get_list_matrix(scene_address,(E_x+l/2,E_y+l/2,z_max,E_x-l/2,E_y-l/2,z_min))
    print(Eye_Window)
    #np.savetxt('/Users/Fangyu/Desktop/Score_Eye_Eindow.txt',Eye_Window,delimiter=' ')
    item_x_max,item_y_max,item_z_max,item_x_min,item_y_min,item_z_min,table_num_in=get_info_with_data(Eye_Window)
    P_in=float(table_num_in)/float(point_num)

    E=(abs(item_x_max-item_x_min))*(abs(item_y_max-item_y_min))*(abs(item_z_max-item_z_min))/(l*l*h)

    if(0.5>P_in>0.3):
        E=E*0.1
    if(0.8>P_in>0.5):
        E=E*0.5
    if(P_in>=0.3):
        E=E*0.01
    else:
        pass
    np.savetxt('/Users/Fangyu/Desktop/Score_'+str(E)+'.txt',Eye_Window,delimiter=' ')



scene_address='/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Aligned_Version_v1.1-4/Aligned_Version/Area_1/office_11/office_11_labelled.txt'

data_list=os.listdir('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Aligned_Version_v1.1-4/Aligned_Version/Area_1/office_11/Annotations')
table_count=0
chair_count=0
for name in data_list:
    if 'table' in name:
        table_address='/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Aligned_Version_v1.1-4/Aligned_Version/Area_1/office_11/Annotations/'+name
        count=0
        while count<=50:
            try:
                Build_and_Evaluate_Eye_Window(table_address,scene_address)
                count+=count
        table_count+=table_count
print(table_count)


'''
找到中心,计算(max(x),max(y),max(z))到中心的距离r,在这个中心周围以r为半径产生一个正态分布，正态分布中抽取的样本作为Eye Window的中心，
以r为参数再产生一个正态分布，样本为Eye Window的边长l。

（包在外面一丁点没关系，多了，比如超过10%，就给一个比较重的处罚）
'''
