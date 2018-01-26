#Kiera McMurtrie
#1/22/2018
#Computer Programming

import random

def mylist():
    mylist1 = []
    mylist1.append('76')
    mylist1.append('92.3')
    mylist1.append('"hello"')
    mylist1.append('True')
    mylist1.append('4')
    mylist1.append('76')
    print(mylist1)
    mylist2 = ['76', '92.3', '"hello"', 'True', '4', '76']
    print(mylist2)

def average():
    mylist = []
    i = 0
    while i <= 100:
        rand = random.randrange(1,1001)
        i = (i+1)
        mylist.append(rand)
        s = sum(mylist)
        s2 = s/100
    print("The average is: " +str(s2))

mylist()
average()
