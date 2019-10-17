# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 21:32:48 2019

@author: marie
"""

dicti={0:'me',1:'Rick',2:'Jamie',3:'Heather',4:'Bryan',5:'Ray',6:'Bas',7:'Patrick',8:'Derek',9:'Joshua'}
Relations=[[0,2,4],[0,1,2],[0,4,0],[0,5,0],[0,7,2],[0,8,0],[0,6,0],[0,9,0],[0,3,8],[1,4,3],[1,6,3],
           [4,6,0],[4,5,0],[5,6,3],[5,7,5],[7,6,7],[6,9,0],[6,3,4],[6,2,0],[8,3,2],[9,3,6],[3,2,9]]
summ=0# sum to sum all values
for i in range(len(dicti)):
   counter=0# reset counter for each new person in the list
   for value in range(len(Relations)):
        mm=Relations[value]
        if i==mm[0] or i==mm[1] :  
            counter+=1      # counter for each personn in the nerwork that is reseted with each new person
        
   summ=summ+counter        # average is the overall sum over the count
       
print("The average number of friends in this network is "+ str(summ//len(dicti)))       #floor the value  
    