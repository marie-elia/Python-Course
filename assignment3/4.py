# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 21:03:38 2019

@author: marie
"""

dicti={0:'me',1:'Rick',2:'Jamie',3:'Heather',4:'Bryan',5:'Ray',6:'Bas',7:'Patrick',8:'Derek',9:'Joshua'}
Relations=[[0,2,4],[0,1,2],[0,4,0],[0,5,0],[0,7,2],[0,8,0],[0,6,0],[0,9,0],[0,3,8],[1,4,3],[1,6,3],
           [4,6,0],[4,5,0],[5,6,3],[5,7,5],[7,6,7],[6,9,0],[6,3,0],[6,2,0],[8,3,2],[9,3,6],[3,2,9]]
strn=[]

for value in range(len(Relations)):
    mm=Relations[value]
    strn.append(mm[2]) # if third value in list is equal to zero then count him in the zero communication people
    if (mm[2]==0):
        print(str(dicti[mm[0]])+" is involved in  " +str(mm[2])+" communication with "+str(dicti[mm[1]]) )   
        
