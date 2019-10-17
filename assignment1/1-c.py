# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 23:25:53 2019

@author: marie
"""
POST=input("enter postal code in this form LDL DLD where L is a letter in [A-Z] and D is a digit in [0-9]")

#first of all check that there is a space in between the first and second 3 chracters
if (POST[3] !=" "):                                   #check at char 3 
    print("can't proceed with checking since there has to be 3 charcters followed by a scape then 3 characters")              # output message for user
else:
    S = POST.replace(" ","")                          # if correct ommit the space to do other checks and save it in a new variable
    ra=S[0:5:2].isupper()                             #ra= true if all letters are uppercase
    if  not(S[1:6:2].isdigit()):                      # check that at positions 1,3,5 they are digits
      print("wrong it has to be a digit")

    elif  ((S[0:5:2].isdigit()) or (ra==False)) :     #check that at positions 0,2,4 it has to be an uppercase letter
      print("wrong it has to be an a letter and uppercase")

    else :                                            #if check is correct then output is correct
      print("correct format")      
