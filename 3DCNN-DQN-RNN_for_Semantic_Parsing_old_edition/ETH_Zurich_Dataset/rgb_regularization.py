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

color_1=color_1.split(' ')
color_2=color_2.split(' ')
color_3=color_3.split(' ')
color_4=color_4.split(' ')
color_5=color_5.split(' ')
color_6=color_6.split(' ')
color_7=color_7.split(' ')
color_8=color_8.split(' ')
color_9=color_9.split(' ')
color_10=color_10.split(' ')
result=open('/Users/Fangyu/Desktop/data/readme.txt','w')

count=0

for item in color_1:
    item=float(item)/255
    item=str(item)
    result.write(item+' ')
    count=count+1
    if count==3:
        result.write('\n')
count=0

for item in color_2:
    item=float(item)/255
    item=str(item)
    result.write(item+' ')
    count=count+1
    if count==3:
        result.write('\n')
count=0


for item in color_3:
    item=float(item)/255
    item=str(item)
    result.write(item+' ')
    count=count+1
    if count==3:
        result.write('\n')
count=0

for item in color_4:
    item=float(item)/255
    item=str(item)
    result.write(item+' ')
    count=count+1
    if count==3:
        result.write('\n')
count=0

for item in color_5:
    item=float(item)/255
    item=str(item)
    result.write(item+' ')
    count=count+1
    if count==3:
        result.write('\n')

count=0

for item in color_6:
    item=float(item)/255
    item=str(item)
    result.write(item+' ')
    count=count+1
    if count==3:
        result.write('\n')
count=0

for item in color_7:
    item=float(item)/255
    item=str(item)
    result.write(item+' ')
    count=count+1
    if count==3:
        result.write('\n')
count=0

for item in color_8:
    item=float(item)/255
    item=str(item)
    result.write(item+' ')
    count=count+1
    if count==3:
        result.write('\n')

count=0

for item in color_9:
    item=float(item)/255
    item=str(item)
    result.write(item+' ')
    count=count+1
    if count==3:
        result.write('\n')
count=0

for item in color_10:
    item=float(item)/255
    item=str(item)
    result.write(item+' ')
    count=count+1
    if count==3:
        result.write('\n')
'''
result.write(float(color_1[0])/255,float(color_1[1])/255,float(color_1[2])/255)
result.write(float(color_2[0])/255,float(color_2[1])/255,float(color_2[2])/255)
result.write(float(color_3[0])/255,float(color_3[1])/255,float(color_3[2])/255)
result.write(float(color_4[0])/255,float(color_4[1])/255,float(color_4[2])/255)
result.write(float(color_5[0])/255,float(color_5[1])/255,float(color_5[2])/255)
result.write(float(color_6[0])/255,float(color_6[1])/255,float(color_6[2])/255)
result.write(float(color_7[0])/255,float(color_7[1])/255,float(color_7[2])/255)
result.write(float(color_8[0])/255,float(color_8[1])/255,float(color_8[2])/255)
result.write(float(color_9[0])/255,float(color_9[1])/255,float(color_9[2])/255)
result.write(float(color_10[0])/255,float(color_10[1])/255,float(color_10[2])/255)
'''
result.close()
