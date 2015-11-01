# _*_ coding: utf-8 _*_

import sys, csv
csvfile = sys.argv[1]

file = open(csvfile, 'r')
dataReader = csv.reader(file)
#count = 00
for data in dataReader:
    id = data[0]
    host = data[1]
    ip = data[2]
    item = data[3]
    key= data[4]

    #    for row in data[1]:
    #        print row
    #    count += 1

file.close()
