import scipy.io as sio


output_office_data=open('/Users/Fangyu/Desktop/office_16_output.txt','r')
visualization=open('/Users/Fangyu/Desktop/test_120.txt','w')


count=0
for line in output_office_data:
    row=line[:-1]
    row=row.split(' ')
    label=row[6]
    if label[0]='1':
        r=41
        g=36
        b=33

    if label[1]='1':
        r=240
        g=255
        b=255

    if label[2]='1':
        r=255
        g=235
        b=205

    if label[3]='1':
        r=255
        g=97
        b=0

    if label[4]='1':
        r=65
        g=105
        b=255

    if label[5]='1':
        r=127
        g=255
        b=212

    if label[6]='1':
        r=56
        g=94
        b=15

    if label[7]='1':
        r=160
        g=32
        b=240

    if label[8]='1':
        r=25
        g=25
        b=112

    if label[9]='1':
        r=255
        g=0
        b=0



'''
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
'''
    visualization.write(row[0]+' '+row[1]+' '+row[2]+' '+r+' '+g+' '+b+'\n')
    t=0
    while t<40:
        xyz_rgb_nv_spin_label.write(str(data_1[count])+' ')
        t=t+1
        count=count+1
    count=count-40
    t=0
    while t<40:
        xyz_rgb_nv_spin_label.write(str(data_2[count])+' ')
        t=t+1
        count=count+1
    count=count-40
    t=0
    while t<40:
        xyz_rgb_nv_spin_label.write(str(data_3[count])+' ')
        t=t+1
        count=count+1
    xyz_rgb_nv_spin_label.write(row[9]+'\n')
