# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 03:01:04 2019

@author: marie
"""

gpa= float(input("Enter your GPA "))#ask user to enter gpa and typecast input to float

if gpa >4.0 or gpa <0.0 : #validate user inpt to be between 0 and 4
  print("GPA must be between 0 and 4")#show warning message to user 
  gpa= float(input("ReEnter your GPA ")) #ask user to reenter gpa if not within range
  #show output according to entered gpa
if gpa>=3.0 and gpa<=4.0:  #[3,4]
  print("superb!")
elif gpa>=2.0 and gpa<3.0: #[2,3[
        print("good!") 
elif gpa>=1.0 and gpa<2.0: #[1,2[
        print("hmmm!")   
elif gpa<1.0 and gpa>=0.0: #[0,1[
        print("no comment!")

  