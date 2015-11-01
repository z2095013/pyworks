# coding: UTF-8

from datetime import date
now = date.today()
birthday = date(1985,6,1)
days = (now - birthday).days #timedelta型

print '生まれてから今日までの日数'
print str(days) + '日'


# zabbix用変換
from datetime import datetime,date
date = str(datetime.today()).split('.')[0]
day = date.split(' ')[0]
time = 'T' + date.split(' ')[1] + 'Z'
print day + time


# 作成中
from datetime import datetime,date
tmp = str(datetime.today()).split('.')[0].split(' ')
tmp.insert(1,'T')
tmp.insert(1,'Z')

print tmp
