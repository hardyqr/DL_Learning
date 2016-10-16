import scipy.io as sio

mat1 = '/Volumes/Seagate Backup Plus Drive/sli/classify_rgboffice16/output_office16/work/pcl/desc/office16_spinImagePC_splittrain_imSiz=0.5.mat'
mat2 = '/Volumes/Seagate Backup Plus Drive/sli/classify_rgboffice16/output_office16/work/pcl/desc/office16_spinImagePC_splittrain_imSiz=0.06.mat'
mat3 = '/Volumes/Seagate Backup Plus Drive/sli/classify_rgboffice16/output_office16/work/pcl/desc/office16_spinImagePC_splittrain_imSiz=1.2.mat'

office_data=open('/Users/Fangyu/Desktop/office_16_nv_l.txt','r')
xyz_rgb_nv_spin_label=open('/Users/Fangyu/Desktop/test_120.txt','w')

data1 = sio.loadmat(mat1)
data2 = sio.loadmat(mat2)
data3 = sio.loadmat(mat3)


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
