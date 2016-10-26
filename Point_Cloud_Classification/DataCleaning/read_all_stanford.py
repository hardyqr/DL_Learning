'''
import os
count=1
Area_1=os.listdir('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Aligned_Version_v1.1-4/Aligned_Version/Area_1')

for room in Area_1:
    if room[0:3] != 'Ico'  and room != '.DS_Store':
        names=os.listdir('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Aligned_Version_v1.1-4/Aligned_Version/Area_1/'+room+'/Annotations')
        out=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/labelled/room_'+str(count)+'.txt','w')
            #out_test=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/labelled/office_1_window.txt','w')

        for name in names:
            if name[0:3] !='Ico' and name != '.DS_Store':
                data=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/original_data/Aligned_Version_v1.1-4/Aligned_Version/Area_1/'+room+'/Annotations/'+name,'r')
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
                if name[0:3]=='wal':
                    label=10
                if name[0:3]=='win':
                    label=11
                for line in data:
                    out.write(line[:-1]+' '+str(label)+'\n')
                data.close()
        out.close()
        count=count+1
'''
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
#输出数据检验
data=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/labelled/room_22.txt','r')

clutter=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/labelled/clutter.txt','w')
beam=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/labelled/beam.txt','w')
board=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/labelled/board.txt','w')
bookcase=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/labelled/bookcase.txt','w')
ceiling=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/labelled/ceiling.txt','w')
chair=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/labelled/chair.txt','w')
column=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/labelled/column.txt','w')
door=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/labelled/door.txt','w')
floor=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/labelled/floor.txt','w')
table=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/labelled/table.txt','w')
wall=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/labelled/wall.txt','w')
window=open('/Volumes/Liu\'s TOSHIBA EXT/database/Stanford_Indoor_Semantic_Parsing/labelled/window.txt','w')

for line in data:
    row=line.split(' ')
    #print(row)
    if row[6]=='0\n':
        clutter.write(line)

    if row[6]=='1\n':
        beam.write(line)

    if row[6]=='2\n':
        board.write(line)

    if row[6]=='3\n':
        bookcase.write(line)

    if row[6]=='4\n':
        ceiling.write(line)

    if row[6]=='5\n':
        chair.write(line)

    if row[6]=='6\n':
        column.write(line)

    if row[6]=='7\n':
        door.write(line)

    if row[6]=='8\n':
        floor.write(line)

    if row[6]=='9\n':
        table.write(line)

    if row[6]=='10\n':
        wall.write(line)

    if row[6]=='11\n':
        window.write(line)
