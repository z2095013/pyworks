# coding: UTF-8

import xml.etree.ElementTree as et

# ファイルを指定
tree = et.parse('test.xml')

# 要素の検索 ツリーの順を定義
#temp1 = tree.find('./templates')
#temp2 = temp1.find('./template')
#temp3 = temp2.find('./items')

# アイテムタグを取得
temp = tree.find('templates/template/items/item')
tags =  temp.getchildren()
for itag in tags:
    print itag.tag    # 出力

# itemツリーを取得
items = tree.findall('templates/template/items/item')
for i in items:

# アイテム名を取得
    iname = i.findall('./name')
    for n in iname:
        print n.text    # 出力
