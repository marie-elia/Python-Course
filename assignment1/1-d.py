# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 03:34:24 2019

@author: marie
"""
#the user inputs a string composed of certain charcters
string=input("Enter a string composed of lowercase a ,b,c ")
countera= string.count('a')#counter for letter a
counterb=string.count('b') #counter for letter b
counterc=string.count('c') #counter for letter c
count=len(string)-countera-counterb-counterc #counter for other letter 

# output result
print("There are "+str(countera)+ " a") 
print("There are "+str(counterb)+ " b")
print("There are "+str(counterc)+ " c")
print("There are "+str(count)+ " other characters")

