import os
from sklearn.cluster import Birch
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

all_offices=os.listdir('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Aligned_Version_v1.1-4/Aligned_Version/Area_1')
print(all_office)
for office in all_offices:

    if office[0:3]=='off':
        num=office[7:]
        print(num)
        all_name=os.listdir('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Aligned_Version_v1.1-4/Aligned_Version/Area_1/'+office+'/Annotations')
        clutters=[]
        tables=[]
        for name in all_name:
            if name[0:3]=='clu':
                clutters.append(name)
            if name[0:3]=='tab':
                tables.append(name)



        def dataloader(output_office_data):
            xs=[]
            ys=[]
            zs=[]
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
                xs.append(float(x))
                ys.append(float(y))
                zs.append(float(z))
                data.append(this)
            return data,xs,ys,zs


        table_centers=[]
        count=1
        for table in tables:
            print(table)
            data=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Aligned_Version_v1.1-4/Aligned_Version/Area_1/'+office+'/Annotations/'+table,'r')
            mid,xs,ys,zs=dataloader(data)

            clf = KMeans(n_clusters=1)
            z_mean=np.mean(zs)#kmeans只能求二维x，y平面内距离，此处求z均值作为后面判断距离的依据
            y_pred = clf.fit_predict(mid)
            table_centers.append([clf.cluster_centers_,count,z_mean])
            count=count+1


        clutter_centers=[]
        count=1
        for clutter in clutters:
            print(clutter)
            data=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Aligned_Version_v1.1-4/Aligned_Version/Area_1/'+office+'/Annotations/'+clutter,'r')
            mid,xs,ys,zs=dataloader(data)

            clf = KMeans(n_clusters=1)
            y_pred = clf.fit_predict(mid)
            z_mean=np.mean(zs)#kmeans只能求二维x，y平面内距离，此处求z均值作为后面判断距离的依据
            clutter_centers.append([clf.cluster_centers_,count,z_mean])
            count=count+1

        relations=[]
        for table_center in table_centers:
            for clutter_center in clutter_centers:
                dist_k_means_center = np.linalg.norm(table_center[0] - clutter_center[0])
                dist_z_avg=np.linalg.norm(table_center[2]-clutter_center[2])
                if dist_k_means_center<1.2 and dist_z_avg< 1:#k_means中心距离小于1.5，z上平均值距离小于1.2判定为属于同一个cluster
                    relations.append([table_center[1],clutter_center[1]])

        print(relations)





        count_table=1
        for table in tables:
            count_clutter=1
            table_data=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Aligned_Version_v1.1-4/Aligned_Version/Area_1/'+office+'/Annotations/'+table,'r')
            table_output=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/labelled/Clutter_Added/office_'+num+'_'+table[:-4]+'_'+'added.txt','w')
            for line in table_data:
                table_output.write(line)

            for clutter in clutters:
                for relation in relations:
                    if count_table == relation[0] and count_clutter == relation[1]:
                        print('yes')

                        clutter_data=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Aligned_Version_v1.1-4/Aligned_Version/Area_1/'+office+'/Annotations/'+clutter,'r')
                        for line in clutter_data:
                            table_output.write(line)
                        clutter_data.close()
                count_clutter=count_clutter+1
            count_table=count_table+1

            table_data.close()
            table_output.close()





        '''Visualization'''
        '''
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(xs,ys,zs,c=y_pred, marker='x')
        plt.title("Kmeans Data")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_ylabel("z")
        plt.show()
        '''
