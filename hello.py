# coding: UTF-8

# 変数 (データにつけるラベル)
msg = "hello world"
print msg


# 数値
print 10 * 5 # 50
print 10 // 3 # 3
print 10 % 3 # 1
print 2 ** 3 # 8
# 整数と少数の演算 → 少数
print 5 + 2.0
# 整数同士の割り算 → 切り捨ての整数
print 10 / 3


# 文字列
# 日本語 u"こんにちわ！"
print "hello " + "world"
print u"無駄！" * 10
print 'hello\n wo\trld\\ it\' a pen'

print """<html lang="ja">
<body>
<\body>
<\html>"""

# 文字列 len
# 検索 find
# 切り出し [] [start:end]
s = "abcdefghi"
print len(s)
print s.find("c")
print s[2]
print s[2:5]
print s[3:-1]
print s[3:]



# 数値 <> 文字列
# 文字列 → 数値 int float
# 数値 → 文字列 str
print 5 + float("5")

age = 20
print "i am " + str(age) + " years old!"

#  リスト
sales = [255, 100, 353, 400]
# len + * []
print len(sales) # 4
print sales[2] # 353
sales[2] = 100
print sales[2] # 100

# in
print 100 in sales # True

# range
print range(10)
print range(3, 10, 2)

# sort / reverse
sales.sort()
print sales

sales.sort()
sales.reverse()
print sales

# 文字列とリスト
d = "2015/09/27"
print d.split("/")

a = ["a", "b", "c"]
print "-".join(a)

# タプル(変更ができない)
a = (2,  5, 8)
# len + * []
print len(a) # 3
print a * 3
# a[2] = 10

#  タプル <> リスト
b = list(a)
print b
c = tuple(b)
print c


# セット（集合型） - 重複を許さない





# データ型



# 真偽値
#
