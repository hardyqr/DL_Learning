import scipy.io as sio


output_office_data=open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/Training_Cleaned/XYZ_Intensity_RGB_Label/bildstein_station1/bildstein_station1_label8.txt','r')
'''
label_0=open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/Training_Cleaned/XYZ_Intensity_RGB_Label/neugasse_station1/neugasse_station1_label0.txt','w')
label_1=open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/Training_Cleaned/XYZ_Intensity_RGB_Label/neugasse_station1/neugasse_station1_label1.txt','w')
label_2=open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/Training_Cleaned/XYZ_Intensity_RGB_Label/neugasse_station1/neugasse_station1_label2.txt','w')
label_3=open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/Training_Cleaned/XYZ_Intensity_RGB_Label/neugasse_station1/neugasse_station1_label3.txt','w')
label_4=open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/Training_Cleaned/XYZ_Intensity_RGB_Label/neugasse_station1/neugasse_station1_label4.txt','w')
label_5=open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/Training_Cleaned/XYZ_Intensity_RGB_Label/neugasse_station1/neugasse_station1_label5.txt','w')
label_6=open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/Training_Cleaned/XYZ_Intensity_RGB_Label/neugasse_station1/neugasse_station1_label6.txt','w')
label_7=open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/Training_Cleaned/XYZ_Intensity_RGB_Label/neugasse_station1/neugasse_station1_label7.txt','w')
label_8=open('/Volumes/Liu\'s TOSHIBA EXT/database/ETH_Zurich_Dataset/semantic-8/Training_Cleaned/XYZ_Intensity_RGB_Label/neugasse_station1/neugasse_station1_label8.txt','w')
'''
'''
{
0: unlabeled points,
1: man-made terrain,人造地面（主要是路）
2: natural terrain,自然地面（主要是草）
3: high vegetation,高植被（主要是树）
4: low vegetation,低植被（主要是草丛）
5: buildings,
6: hard scape,硬质景观（矮墙，墓碑(第一个scene)，栏杆）
7: scanning artefacts,（人）
8: cars
}
'''
import csv

mid_file = open('/Users/Fangyu/Desktop/mid_data.csv', 'w')



data=[]
for line in output_office_data:
    this=[]
    row=line[:-1]
    row=row.split(' ')
    x=row[0]
    y=row[1]
    z=row[2]
    #mid_file.write(x+','+y+'\n')
    this.append(float(x))
    this.append(float(y))
    data.append(this)
#mid_file.close()

print(data)

from sklearn.cluster import Birch
from sklearn.cluster import KMeans


'''
KMeans
'''
'''
clf = KMeans(n_clusters=3) 表示类簇数为3，聚成3类数据，clf即赋值为KMeans
y_pred = clf.fit_predict(X) 载入数据集X，并且将聚类的结果赋值给y_pred
'''

clf = KMeans(n_clusters=4)
y_pred = clf.fit_predict(data)

#输出完整Kmeans函数，包括很多省略参数
print(clf)
#输出聚类预测结果，20行数据，每个y_pred对应X一行或一个球员，聚成3类，类标为0、1、2
print(y_pred)


'''
Visualization
'''
import matplotlib.pyplot as plt
plt.scatter(x, y, c=y_pred, marker='x')
plt.title("Kmeans-Basketball Data")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

'''
#didn't find "KMeansClassifier"
import pandas as pd
import numpy as np
from kmeans import KMeansClassifier
import matplotlib.pyplot as plt

#加载数据集，DataFrame格式，最后将返回为一个matrix格式
def loadDataset(infile):
    df = pd.read_csv(infile, sep='\t', header=0, dtype=str, na_filter=False)
    return np.array(df).astype(np.float)

if __name__=="__main__":
    data_X = loadDataset(r"/Users/Fangyu/Desktop/mid_data.txt")
    k = 4#设定聚类中心个数
    clf = KMeansClassifier(k)
    clf.fit(data_X)
    cents = clf._centroids
    labels = clf._labels
    sse = clf._sse
    colors = ['b','g','r','k','c','m','y','#e24fff','#524C90','#845868']
    for i in range(k):
        index = np.nonzero(labels==i)[0]
        x0 = data_X[index, 0]
        x1 = data_X[index, 1]
        y_i = i
        for j in range(len(x0)):
            plt.text(x0[j], x1[j], str(y_i), color=colors[i], \
                        fontdict={'weight': 'bold', 'size': 6})
        plt.scatter(cents[i,0],cents[i,1],marker='x',color=colors[i],\
                    linewidths=7)

    plt.title("SSE={:.2f}".format(sse))
    plt.axis([-7,7,-7,7])
    outname = "/Users/Fangyu/Desktop/k_clusters" + str(k) + ".png"
    plt.savefig(outname)
    plt.show()
'''
'''
    if label=='0':
        label_0.write(row[0]+' '+row[1]+' '+row[2]+' '+row[3]+' '+row[4]+' '+row[5]+' '+row[6]+'\n')

    if label=='1':
        label_1.write(row[0]+' '+row[1]+' '+row[2]+' '+row[3]+' '+row[4]+' '+row[5]+' '+row[6]+'\n')


    if label=='2':
        label_2.write(row[0]+' '+row[1]+' '+row[2]+' '+row[3]+' '+row[4]+' '+row[5]+' '+row[6]+'\n')


    if label=='3':
        label_3.write(row[0]+' '+row[1]+' '+row[2]+' '+row[3]+' '+row[4]+' '+row[5]+' '+row[6]+'\n')


    if label=='4':
        label_4.write(row[0]+' '+row[1]+' '+row[2]+' '+row[3]+' '+row[4]+' '+row[5]+' '+row[6]+'\n')


    if label=='5':
        label_5.write(row[0]+' '+row[1]+' '+row[2]+' '+row[3]+' '+row[4]+' '+row[5]+' '+row[6]+'\n')


    if label=='6':
        label_6.write(row[0]+' '+row[1]+' '+row[2]+' '+row[3]+' '+row[4]+' '+row[5]+' '+row[6]+'\n')


    if label=='7':
        label_7.write(row[0]+' '+row[1]+' '+row[2]+' '+row[3]+' '+row[4]+' '+row[5]+' '+row[6]+'\n')


    if label=='8':
        label_8.write(row[0]+' '+row[1]+' '+row[2]+' '+row[3]+' '+row[4]+' '+row[5]+' '+row[6]+'\n')

label_0.close()
label_1.close()
label_2.close()
label_3.close()
label_4.close()
label_5.close()
label_6.close()
label_7.close()
label_8.close()
'''
output_office_data.close()
