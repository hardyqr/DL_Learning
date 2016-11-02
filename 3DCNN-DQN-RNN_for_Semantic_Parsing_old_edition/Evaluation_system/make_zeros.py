#11/2/2016
#Fangyu
#this program produces data with zero scores for training 3DCNN
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.cluster import Birch
#from sklearn.cluster import KMeans
import os
from get_info import *
path='/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/'
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
def _in_scene_(x,y,z,l,i_max_x,i_max_y,i_max_z,i_min_x,i_min_y,i_min_z):
    if (x+l/2<i_max_x and y+l/2<i_max_y and z+l/2<i_max_z and x+l/2>i_min_x and y+l/2>i_min_y and z+l/2>i_min_z)\
        or (x-l/2<i_max_x and y-l/2<i_max_y and z-l/2<i_max_z and x-l/2>i_min_x and y-l/2>i_min_y and z-l/2>i_min_z)\
        or (x-l/2<i_max_x and y+l/2<i_max_y and z+l/2<i_max_z and x-l/2>i_min_x and y+l/2>i_min_y and z+l/2>i_min_z)\
        or (x+l/2<i_max_x and y-l/2<i_max_y and z+l/2<i_max_z and x+l/2>i_min_x and y-l/2>i_min_y and z+l/2>i_min_z)\
        or (x+l/2<i_max_x and y+l/2<i_max_y and z-l/2<i_max_z and x+l/2>i_min_x and y+l/2>i_min_y and z-l/2>i_min_z)\
        or (x+l/2<i_max_x and y-l/2<i_max_y and z-l/2<i_max_z and x+l/2>i_min_x and y-l/2>i_min_y and z-l/2>i_min_z)\
        or (x-l/2<i_max_x and y-l/2<i_max_y and z+l/2<i_max_z and x-l/2>i_min_x and y-l/2>i_min_y and z+l/2>i_min_z)\
        or (x-l/2<i_max_x and y+l/2<i_max_y and z-l/2<i_max_z and x-l/2>i_min_x and y+l/2>i_min_y and z-l/2>i_min_z):
        #if a corner is in the scene
        return True
    else:return False

def _in_item_(x,y,z,l,i_max_x,i_max_y,i_max_z,i_min_x,i_min_y,i_min_z):
    if (x+l/2<i_max_x and y+l/2<i_max_y and z+l/2<i_max_z and x+l/2>i_min_x and y+l/2>i_min_y and z+l/2>i_min_z)\
        or (x-l/2<i_max_x and y-l/2<i_max_y and z-l/2<i_max_z and x-l/2>i_min_x and y-l/2>i_min_y and z-l/2>i_min_z)\
        or (x-l/2<i_max_x and y+l/2<i_max_y and z+l/2<i_max_z and x-l/2>i_min_x and y+l/2>i_min_y and z+l/2>i_min_z)\
        or (x+l/2<i_max_x and y-l/2<i_max_y and z+l/2<i_max_z and x+l/2>i_min_x and y-l/2>i_min_y and z+l/2>i_min_z)\
        or (x+l/2<i_max_x and y+l/2<i_max_y and z-l/2<i_max_z and x+l/2>i_min_x and y+l/2>i_min_y and z-l/2>i_min_z)\
        or (x+l/2<i_max_x and y-l/2<i_max_y and z-l/2<i_max_z and x+l/2>i_min_x and y-l/2>i_min_y and z-l/2>i_min_z)\
        or (x-l/2<i_max_x and y-l/2<i_max_y and z+l/2<i_max_z and x-l/2>i_min_x and y-l/2>i_min_y and z+l/2>i_min_z)\
        or (x-l/2<i_max_x and y+l/2<i_max_y and z-l/2<i_max_z and x-l/2>i_min_x and y+l/2>i_min_y and z-l/2>i_min_z)\
        or (x+l/2>i_max_x and y+l/2>i_max_y and z+l/2>i_max_z and x-l/2<i_min_x and y-l/2<i_min_y and z-l/2<i_min_z):
        #if a corner is in the scene or eye window includes the scene
        return True
    else:return False


def Build_Eye_Window_with_zero_scores(table_address,scene_address,item_name,scene_name,num):
    i_x_max,i_y_max,i_z_max,i_x_min,i_y_min,i_z_min,i_x_mean,i_y_mean,i_z_mean,i_point_num=get_item_info(table_address)

    E_x=np.random.normal(loc=i_x_mean, scale=1, size=None)
    E_y=np.random.normal(loc=i_y_mean, scale=1, size=None)
    E_z=np.random.normal(loc=i_z_mean, scale=1, size=None)
    l=E_l=abs(np.random.normal(loc=max(abs(i_x_max-i_x_min),abs(i_y_max-i_y_min),abs(i_z_max-i_z_min)), scale=1.0, size=None))

    x_max,y_max,z_max,x_min,y_min,z_min,x_mean,y_mean,z_mean,point_num=get_item_info(scene_address)
    length=0
    while(length==0):#if in item or not in scene, rebuild E_x,E_y,_E_z,l

        if (not _in_item_(E_x,E_y,E_z,l,i_x_max,i_y_max,i_z_max,i_x_min,i_y_min,i_z_min)) and (_in_scene_(E_x,E_y,E_z,l,x_max,y_max,z_max,x_min,y_min,z_min)):
            #if in scene and not in item, and length is greater than zero, obtain data
            print(E_x,E_y,E_z,l,E_l)
            Eye_Window=get_list_matrix(scene_address,(E_x+l/3,E_y+l/3,E_z+l/3,E_x-l/3,E_y-l/3,E_z-l/3))
            print(Eye_Window)
            length=len(Eye_Window)
            if length!=0:
                np.savetxt(path+'table_training/Score_0.0/'+scene_name+'_'+item_name+'_'+str(num)+'_Score_0.0.txt',Eye_Window,delimiter=' ')
            else:
                E_x=np.random.normal(loc=i_x_mean, scale=1, size=None)
                E_y=np.random.normal(loc=i_y_mean, scale=1, size=None)
                E_z=np.random.normal(loc=i_z_mean, scale=1, size=None)
                l=E_l=abs(np.random.normal(loc=max(abs(i_x_max-i_x_min),abs(i_y_max-i_y_min),abs(i_z_max-i_z_min)), scale=1.0, size=None))
        else:
            E_x=np.random.normal(loc=i_x_mean, scale=1, size=None)
            E_y=np.random.normal(loc=i_y_mean, scale=1, size=None)
            E_z=np.random.normal(loc=i_z_mean, scale=1, size=None)
            l=E_l=abs(np.random.normal(loc=max(abs(i_x_max-i_x_min),abs(i_y_max-i_y_min),abs(i_z_max-i_z_min)), scale=1.0, size=None))


scenes=path+'original_data/Stanford3dDataset_v1.1-5/Area_4/'
scene_list=os.listdir(scenes)
for scene in scene_list:
    if 'office' in scene:
        scene_address=scenes+scene
        items_list=os.listdir(scene_address+'/Annotations/')
        table_count=0
        for item in items_list:
            if 'table' in item:
                table_count+=1
        for item in items_list:
            if table_count==1 and 'table' in item:
                table_address=scene_address+'/Annotations/'+item
                count=0
                while count<=50:
                    #try:
                    Build_Eye_Window_with_zero_scores(table_address,scene_address+'/'+scene+'_labelled.txt',item[:-4],scene,count)
                    count+=1
                    #except:
                    #    print('fail')
