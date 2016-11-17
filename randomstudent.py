#!/usr/bin/python

import random

#making lists bc choice is looking at the lists as integers
#CLASSES =  { 
pd4= [ 'Ayman', 'Shaeq', 'Patrick', 'Yvonne', 'Wilson',
         'Brian', 'Farhan', 'Janet', 'Harry', 'Kevin',
         'Nicholas', 'Jason', 'Yikai', 'Emma', 'Kenneth',
         'Nala', 'Karol', 'Elias', 'Ely', 'Reo', 'Dhriaj',
         'Amy', 'Arvind', 'Nobel', 'Angela', 'Edward',
         'Jonathan', 'Celine', 'Daniel', 'Lindsey', 'Ziyan', 'Elina']

pd8= ['Julian', 'Sebastian', 'Jordan', 'Alan', 'Yuki',
        'Chloe', 'Noah', 'Edvic', 'Jia Qi', 'Shan', 'Rodda',
        'Anya', 'Edmond', 'Asher', 'Kathy', 'Sharon', 'Vincent',
        'Lawrence', 'Sachal', 'Gabriel', 'Jason', 'Daniel',
        'Felix', 'Jacob', 'Bayle', 'Fortune', 'Gio',
        'Kelly', 'William', 'Jordan', 'Haley', 'Henry']

pd9= ['James', 'Vanna', 'Zicheng', 'Quinn', 'Anthony C',
        'Joel', 'Steph', 'Xinhui', 'Richard', 'Misha',
        'Maddie', 'Winston', 'Shariar', 'Nancy', 'Jerry',
        'Michael', 'Stiven', 'Will',  'Olivia', 'Constantine',
        'Jessica', 'Kate', 'Shamaul', 'Max', 'Sarah', 'Anthony L',
        'Brandon', 'Nicole', 'Brian', 'Issac', 'Seiji', 'Lorenz']
#}

def randomStu(pd):
    print random.choice(pd)

print
print
print("period 4")
randomStu(pd4)
randomStu(pd4)
randomStu(pd4)
randomStu(pd4)

print
print
print("period 8")
randomStu(pd8)
randomStu(pd8)
randomStu(pd8)
randomStu(pd8)

print
print
print("period 9")
randomStu(pd9)
randomStu(pd9)
randomStu(pd9)
randomStu(pd9)

