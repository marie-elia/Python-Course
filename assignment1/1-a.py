# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:09:24 2019

@author: marie
"""

x=int(input("Enter first value "))
y=int(input("Enter second value "))
#find cartesian product of 2 numbers
maximum=max(x,y) #get max of 2 values
minimum=min(x,y) #get min of 2 values
print("The permutations for "+str(x)+" and "+str(y)+" are :")
for i in range (minimum+1):
    for j in range (maximum+1):
        print(i,end='')          
        print(j,end='  ')
#get cartesian product   
# if input is 2 and 3 then The permutations for 2 and 3 are: 00  01  02  03  10  11  12  13  20  21  22  23 
  
