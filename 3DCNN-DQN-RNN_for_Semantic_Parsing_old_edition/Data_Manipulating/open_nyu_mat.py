import scipy.io as sio
import h5py

mat = '/Volumes/Liu\'s TOSHIBA EXT/database/nyu_depth_v2_labeled.mat'

f = h5py.File(mat)
f.keys()
#office_data=open('/Users/Fangyu/Desktop/office_16_nv_l.txt','r')
#xyz_rgb_nv_spin_label=open('/Users/Fangyu/Desktop/test_120.txt','w')

#data = sio.loadmat(mat)
'''
data1=data1['desc'].T
data2=data2['desc'].T
data3=data3['desc'].T

data_1=[]
data_2=[]
data_3=[]

for line in data1:
    for item in line:
        data_1.append(item)


for line in data2:
    for item in line:
        data_2.append(item)
for line in data3:
    for item in line:
        data_3.append(item)

count=0
for line in office_data:
    row=line[:-1]
    row=row.split(' ')
    xyz_rgb_nv_spin_label.write(row[0]+' '+row[1]+' '+row[2]+' '+row[3]+' '+row[4]+' '+row[5]+' '+row[6]+' '+row[7]+' '+row[8]+' ')
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
'''
#type(f)
print(f['scenes'].T)
for line in f['scenes'].T:
    print(line)
