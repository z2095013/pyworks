# _*_ coding: utf-8 _*_
import sys
xmlfile = str(sys.argv[1]).split('.')[0] + '.xml'

# 作成日
from datetime import datetime,date
date = str(datetime.today()).split('.')[0]
day = date.split(' ')[0]
time = 'T' + date.split(' ')[1] + 'Z'
# print day + time

# xmlノード作成
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, dump, parse, ElementTree
from xml.dom import minidom


# ルート
zabbix = Element('zabbix_export')

# バージョン
version = SubElement(zabbix, 'version')
version.text = '2.0'


# 日付
date = SubElement(zabbix, 'date')
date.text = day + time


# グループ
groups = SubElement(zabbix, 'groups')
group = SubElement(groups, 'group')
groupname = SubElement(group, 'name')
groupname.text = 'AAA'


# テンプレート
templates = SubElement(zabbix, 'templates')
template = SubElement(templates, 'template')
templatechild = SubElement(template, 'template')
templatechild.text = 'BBB'
#templatechild.set = ('discription', 'BBB')

templatename = SubElement(template, 'name')
templatename.text = 'CCC'

# アイテム

#dump(zabbix)
#print tostring(zabbix)

# xmlファイル書き込み
#tree = ElementTree(zabbix)
#tree.write(xmlfile, 'UTF-8', 'True') #改行なし

f = open(xmlfile, 'w')
tree = minidom.parseString(tostring(zabbix)).toprettyxml()
#print tree
f.write(tree)
f.close()
