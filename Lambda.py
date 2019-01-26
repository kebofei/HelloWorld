#!/usr/bin/python
# -*- coding: UTF-8 -*-

li=[{'age':20,'name':'def'},{'age':25,'name':'abc'},{'age':10,'name':'ghi'}]
li = sorted(li,key=lambda x:x['age'])
print(li)

a = [('a',1),('b',2),('c',3),('d',4)]
a_1 = list(map(lambda x:x[0],a))
print(a_1)

a2 = [1,2,3,4,5,6,7,8]
a_2 = list(filter(lambda x:x<4,a2))
print(a_2)

dict = {'a':1,'c':7,'b':8,'d':4,'f':3,'e':6}
sorted_dict_asc = sorted(dict.items(),key=lambda x:x[0])
print(sorted_dict_asc)