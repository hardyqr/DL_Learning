
import numpy
import random


data_with_label= open('/Users/Fangyu/Desktop/office_16.txt','r')
data_with_rgb_label=open('/Users/Fangyu/Desktop/data/office_16_rgb_label.txt','w')
data_xyz_rgb=open('/Users/Fangyu/Desktop/data/office_16_xyz_rgb.txt','w')


color_1='41 36 33' #象牙黑
color_2='240 255 255' #天蓝色
color_3='255 235 205' #白杏仁
color_4='255 97 0' #橙色
color_5='65 105 225' #品蓝
color_6='127 255 212' #碧绿色
color_7='56 94 15' #绿土
color_8='160 32 240' #紫色
color_9='25 25 112' #深蓝色
color_10='255 0 0' #红色


for line in data_with_label:

    row=line[:-1]
    line=row.split(" ")
    if line[6]=='1':
        data_xyz_rgb.write(line[0]+' '+line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+'\n')
        data_with_rgb_label.write(line[0]+' '+line[1]+' '+line[2]+' '+color_1+'\n')
    if line[6]=='2':
        data_xyz_rgb.write(line[0]+' '+line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+'\n')
        data_with_rgb_label.write(line[0]+' '+line[1]+' '+line[2]+' '+color_2+'\n')
    if line[6]=='3':
        data_xyz_rgb.write(line[0]+' '+line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+'\n')
        data_with_rgb_label.write(line[0]+' '+line[1]+' '+line[2]+' '+color_3+'\n')
    if line[6]=='4':
        data_xyz_rgb.write(line[0]+' '+line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+'\n')
        data_with_rgb_label.write(line[0]+' '+line[1]+' '+line[2]+' '+color_4+'\n')
    if line[6]=='5':
        data_xyz_rgb.write(line[0]+' '+line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+'\n')
        data_with_rgb_label.write(line[0]+' '+line[1]+' '+line[2]+' '+color_5+'\n')
    if line[6]=='6':
        data_xyz_rgb.write(line[0]+' '+line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+'\n')
        data_with_rgb_label.write(line[0]+' '+line[1]+' '+line[2]+' '+color_6+'\n')
    if line[6]=='7':
        data_xyz_rgb.write(line[0]+' '+line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+'\n')
        data_with_rgb_label.write(line[0]+' '+line[1]+' '+line[2]+' '+color_7+'\n')
    if line[6]=='8':
        data_xyz_rgb.write(line[0]+' '+line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+'\n')
        data_with_rgb_label.write(line[0]+' '+line[1]+' '+line[2]+' '+color_8+'\n')
    if line[6]=='9':
        data_xyz_rgb.write(line[0]+' '+line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+'\n')
        data_with_rgb_label.write(line[0]+' '+line[1]+' '+line[2]+' '+color_9+'\n')
    if line[6]=='10':
        data_xyz_rgb.write(line[0]+' '+line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+'\n')
        data_with_rgb_label.write(line[0]+' '+line[1]+' '+line[2]+' '+color_10+'\n')


data_with_label.close()
data_with_rgb_label.close()
data_xyz_rgb.close()
