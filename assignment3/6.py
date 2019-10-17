# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 22:56:26 2019

@author: marie
"""

dicti={0:'me',1:'Rick',2:'Jamie',3:'Heather',4:'Bryan',5:'Ray',6:'Bas',7:'Patrick',8:'Derek',9:'Joshua'}
Relations=[[0,2,4],[0,1,2],[0,4,0],[0,5,0],[0,7,2],[0,8,0],[0,6,0],[0,9,0],[0,3,8],[1,4,3],[1,6,3],
           [4,6,0],[4,5,0],[5,6,3],[5,7,5],[7,6,7],[6,9,0],[6,3,4],[6,2,0],[8,3,2],[9,3,6],[3,2,9]]

print("People who have more than 4 friends")         

for i in range(len(dicti)):
   counter=0#resr counter for each iteration
   for value in range(len(Relations)):
        mm=Relations[value]# acess the list
        if i==mm[0] or i==mm[1] :  # if found on any side of the list as first or second item[0,2,2]or[2,0,2]
            counter+=1 #increment counter by one
   if counter>4:     # if counter of frinds is greater than 4 the print me 
       
       print(str(dicti[i])+" has "+str(counter)+" friends")    
       
