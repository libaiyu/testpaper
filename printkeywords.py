# _*_ coding: utf_8  _*_
#! python3
# print key words in python3.

def pkeywords():
    from keyword import kwlist
    for k in range(len(kwlist)):
        print(kwlist[k])
