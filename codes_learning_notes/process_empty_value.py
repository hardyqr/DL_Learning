import csv
#csvfile2 = open('/Users/Fangyu/Desktop/test_processed.csv', 'w')
#csvfile1= open('/Users/Fangyu/Desktop/test.csv', 'r')

csvfile2 = open('/Users/Fangyu/Desktop/train_processed.csv', 'w')
csvfile1= open('/Users/Fangyu/Desktop/train.csv', 'r')
writer = csv.writer(csvfile2)
reader = csv.reader(csvfile1)

for line in reader:
    row=[]
    for item in line:
        item=int(item)
        if item=='':
            item=0
        row.append(item)
    writer.writerow(row)


csvfile1.close()
csvfile2.close()
