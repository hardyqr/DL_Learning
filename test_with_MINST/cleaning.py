import os
count=0
Area_1=os.listdir('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Aligned_Version_v1.1-4/Aligned_Version/Area_1')
print(Area_1)

for room in Area_1:
    if room != 'Icon\r' or '.DS_Store':
        names=os.listdir('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Aligned_Version_v1.1-4/Aligned_Version/Area_1/'+room+'/Annotations')
        out=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/labelled/room_'+str(count)+'.txt','w')
            #out_test=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/labelled/office_1_window.txt','w')

        for name in names:
            if room!='Icon\r' or '.DS_Store':
                data=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Aligned_Version_v1.1-4/Aligned_Version/Area_1/'+room+'/Annotations/'+name,'r')
                print('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Aligned_Version_v1.1-4/Aligned_Version/Area_1/'+room+'/Annotations/'+name)
                if name[0:3]=='clu':
                    label=0
                if name[0:3]=='bea':
                    label=1
                if name[0:3]=='boa':
                    label=2
                if name[0:3]=='boo':
                    label=3
                if name[0:3]=='cei':
                    label=4
                if name[0:3]=='cha':
                    label=5
                if name[0:3]=='col':
                    label=6
                if name[0:3]=='doo':
                    label=7
                if name[0:3]=='flo':
                    label=8
                if name[0:3]=='tab':
                    label=9
                if name[0:3]=='wall':
                    label=10
                if name[0:3]=='win':
                    label=11
                for line in data:
                    out.write(line[:-1]+' '+str(label)+'\n')
                data.close()
        out.close()

'''
            clutter:0
            beam:1
            board:2
            bookcas:3
            ceiling:4
            chair:5
            column:6
            door:7
            floor:8
            table:9
            wall:10
            window:11
'''
