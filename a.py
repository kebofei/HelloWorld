#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 10
print(a)
print('陈汉飞')


# pop()
# del
# remove()

# list3 * 5
# 123 in list3
# 123 not in list3
#

#str2 = 'xiaoxie'
#str2.capitalize()
#'Xiaoxie'

#str2 = 'DAXIE'
#str2.casefold()
#'daxie'

#str2.center(10)
#'  DAXIE   '

#str3
#'chenhan chen han chen'
#str3.endswith('en')
#True
#str3.endswith('s')
#False

#str4='chen\than\tfei'
#str4.expandtabs()
#'chen    han     fei'

#str5='abcdefg'
#str5.find('f')
#5
#str5.find('g')
#6

#str7.partition('s')
#('i ', 's', 'hi zhu')

#str7
#'i shi zhu'
#str7.replace('zhu','dog')
#'i shi dog'

#str8 = '       aaa  bbbbb    '
#str8.strip()
#'aaa  bbbbb'

#str9
#'aaaaabbbbaaaaa'
#str9.translate(str.maketrans('a','c'))
#'cccccbbbbccccc'

#"{0} love {1}.{2}".format("i","GSK","com")
#'i love GSK.com'
#"{a} love {b}.{c}".format(a="i",b="GSK",c="com")
#'i love GSK.com'
#"{0} love {b}.{c}".format("i",b="GSK",c="com")
#i love GSK.com

list  = ['global', 'pythontab.com']
def func1():
    list.append('abcdefg')
    print(list)
func1()
print(list)

list = ['global','pythontab.com']
def func2():
    list = ['docs.abcdef']
    print(list)
func2()
print(list) #局部变量赋值不能改变全局变量的值

print('\t')
list = ['张柳燕','夜的黑']
def func3():
    global list
    list = ['陈寒风']
    print(list)
func3()
print(list)

