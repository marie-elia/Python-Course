# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:56:26 2019

@author: marie
"""

dicti={0:'me',1:'Rick',2:'Jamie',3:'Heather',4:'Bryan',5:'Ray',6:'Bas',7:'Patrick',8:'Derek',9:'Joshua'}
Relations=[[0,2,4],[0,1,2],[0,4,0],[0,5,0],[0,7,2],[0,8,0],[0,6,0],[0,9,0],[0,3,8],[1,4,3],[1,6,3],
           [4,6,0],[4,5,0],[5,6,3],[5,7,5],[7,6,7],[6,9,0],[6,3,0],[6,2,0],[8,3,2],[9,3,6],[3,2,9]]
jj=[]
kk=[]
print("The three highest people involved in some kind of direct communication with others in the network.")
for i in range(len(dicti)):
   strength=0# reset the strength to zero for each iterartion
   for value in range(len(Relations)):
        mm=Relations[value]#mm to acess list
        if i==mm[0] or i==mm[1] : #now acess the value in the list of list  
            strength=strength+mm[2] #accumulate strength fo each person wheter on any side[0,2,2] or [2,0,2] 
   jj.append(strength)
final_list2 = [] # create a list to append values to it

for k in range(0, 3):  # range 3 because i want the highest 3 
        max1 = 0# set maximum value to zero for each iteration
          
        for j in range(len(jj)):      
            if jj[j] > max1: #compare to get highest value 
                max1 = jj[j];
                new=j #once found ,save the index
                max2 =dicti[j] # now get the name related to this index
        jj[new]=0# replace the maximumvalue with zero so that it can't be found again
        final_list2.append(max2) #append names to the list
  
print(final_list2) 
    