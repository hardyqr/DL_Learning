'''
data_label= open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/Ground Truth/sem8_labels_training/bildstein_station1_xyz_intensity_rgb.labels','r')
data=open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/Training Data/bildstein_station1_xyz_intensity_rgb.txt', 'r')
data_with_label=open('//Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/bildstein_station1_xyz_intensity_rgb_label.txt','w')
data_6d=open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/bildstein_station1_xyz_rgb.txt','w')

'''

data_label= open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/Ground Truth/sem8_labels_training/bildstein_station3_xyz_intensity_rgb.labels','r')
data=open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/Training Data/bildstein_station3_xyz_intensity_rgb.txt', 'r')
data_with_label=open('//Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/bildstein_station3_xyz_intensity_rgb_label.txt','w')
data_6d=open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/bildstein_station3_xyz_rgb.txt','w')


'''
data_label= open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/Ground Truth/sem8_labels_training/bildstein_station5_xyz_intensity_rgb.labels','r')
data=open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/Training Data/bildstein_station5_xyz_intensity_rgb.txt', 'r')
data_with_label=open('//Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/bildstein_station5_xyz_intensity_rgb_label.txt','w')
data_6d=open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/bildstein_station5_xyz_rgb.txt','w')
'''
'''
domfountain_station1_xyz_intensity_rgb.txt
domfountain_station2_xyz_intensity_rgb.txt
domfountain_station3_xyz_intensity_rgb.txt

station1_xyz_intensity_rgb.txt
station2_xyz_intensity_rgb.txt
station4_xyz_intensity_rgb.txt
station5_xyz_intensity_rgb.txt
station9_xyz_intensity_rgb.txt

'''
labels=[]
for line in data_label:
    labels.append(line[0])

count=0
for line in data:
    row=line[:-2]
    line=row.split(" ")
    if labels[count]!='0':
        print(labels[count])
        data_with_label.write(line[0]+' '+line[1]+' '+line[2]+' '+line[3]+' '+line[4]+' '+line[5]+' '+line[6]+' '+labels[count]+'\n')
        data_6d.write(line[0]+' '+line[1]+' '+line[2]+' '+line[4]+' '+line[5]+' '+line[6]+'\n')
    count=count+1


data.close()
data_label.close()
data_with_label.close()
data_6d.close()
