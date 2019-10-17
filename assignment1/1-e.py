# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 23:41:56 2019

@author: marie
"""

list=[112,72,69,97,107,73,92,76,86,73,126,128,118,127,124,82,104,132,134,83,92,108,96,100,92,115,76,91,102,81,95,141,81,80,106,84,119,113,98,75,68,98,115,106,95,100,85,94,106,119]  
list.sort() #sort the values
temp=-999999999999999 #store temp as a large value for the first initial stem calculation
for i in range (len(list)):
     mod=int(list[i]%10)  #set modulus
     rem=int(list[i]/10)  #set  remainder

     if(temp==rem): #see if remainder was calculated before then print leaf else it is a new value that the stem is new 
             print (mod,end='  ')
     else:
             print("    ")
             if(rem>9): # just to make it good while printing because with remaining greater than 9 the " | " is shifted by one and it looks bad
                 print (rem,end='  |   ')
             else:
                 print (rem,end='   |   ')  #print stem then leaf because stem was not previously calculated 

             print (mod,end='   ')
     temp=rem
