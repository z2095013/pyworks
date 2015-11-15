# -*- coding: utf-8 -*-

def readcsv():
    import csv
    file = open(csvfile, 'r')
    dataReader = csv.reader(file)
    for data in dataReader:
        id = data[0]
        host = data[1]
        ip = data[2]
        item = data[3]
        key= data[4]
        print data[1]
#        print id, host, ip, item, key
    file.close()

if __name__ == "__main__":
    import sys
    try:
        csvfile = sys.argv[1]
        readcsv()
    except IndexError:
        print 'csvファイルを指定してください。'
