# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 23:05:49 2019

@author: marie
"""

#dictionary to map each person to a number and used number as a key to be able to iterate on the dictionary 

dicti={0:'me',1:'Rick',2:'Jamie',3:'Heather',4:'Bryan',5:'Ray',6:'Bas',7:'Patrick',8:'Derek',9:'Joshua'}
#list of list to mention the relations and their strength
Relations=[[0,2,4],[0,1,2],[0,4,0],[0,5,0],[0,7,2],[0,8,0],[0,6,0],[0,9,0],[0,3,8],[1,4,3],[1,6,3],
           [4,6,0],[4,5,0],[5,6,3],[5,7,5],[7,6,7],[6,9,0],[6,3,4],[6,2,0],[8,3,2],[9,3,6],[3,2,9]]


print("list of all friends of each person in the network:")

for i in range(len(dicti)):
   print(dicti[i]+" is a friend of:" ) #iterate to otput the dictionary in order
   for value in range(len(Relations)): 
       mm=Relations[value]
       if i==mm[0]:    # here i am checking if for example me with key 0 is present as the first or the second number in the list[0,2,2]or [2,0,2] 
           print(dicti[mm[1]],end=' ') #if found I print the other one in the relation
       elif i==mm[1]:
           print(dicti[mm[0]],end=' ')   
   print()    # just for a better looking output
   print()