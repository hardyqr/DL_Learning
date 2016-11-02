#import pandas as pd
import numpy as np

office_data=open('/Users/Fangyu/Desktop/office_16.txt','r')
xs=[]
ys=[]
zs=[]
length=0
office_data_list=[]

for line in office_data:
    row=line[:-1]
    row=row.split(' ')
    xs.append(float(row[0]))
    ys.append(float(row[1]))
    zs.append(float(row[2]))
    length=length+1
    office_data_list.append(line[:-1])

x_max=max(xs)
x_min=min(xs)

y_max=max(ys)
y_min=min(ys)

z_max=max(zs)
z_min=min(zs)

print(x_max,x_min,y_max,y_min,z_max,z_min,x_max-x_min,y_max-y_min,z_max-z_min)

x_max=-8.859
x_min=-11.871
y_max=13.935
y_min=8.751
z_max=3.173
z_min=-0.018

xs=[i/1.0 for i in range(int(abs(x_max)*1000),int(abs(x_min)*1000)+1)]
xs=[-x/1000 for x in xs]
xs=xs[::-1]
ys=[i/1.0 for i in range(int(abs(y_min)*1000),int(abs(y_max)*1000)+1)]
ys=[y/1000 for y in ys]
zs=[i/1.0 for i in range(int(z_min*1000),int(abs(z_max)*1000)+1)]
zs=[z/1000 for z in zs]

count=0

all_groups=[]
print(length)
bigger=max(abs(x_max),abs(x_min))*1000
smaller=min(abs(x_max),abs(x_min))*1000
iters=int(bigger-smaller)
for count in range(iters):
    group=[]
    t=0
    while t<length:
        row=office_data_list[t].split(' ')
        #print(xs[count],float(row[0]),xs[count+1])
        left=xs[count]
        right=xs[count+1]
        if left<=float(row[0])<=right:
            group.append(row[0])
            print(left,row[0],right)
        t=t+1
    count=count+1
    all_groups.append(group)
print(all_groups)
