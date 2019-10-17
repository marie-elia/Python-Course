# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 01:18:59 2019

@author: marie
"""

def duplicateLine(fileName, lineNumber, n):
   'creates n new duplicates of lineNumber (0 indexed) right after this line. '
   try:
        infile = open(fileName)#open file read
   except IOError:
        print ("Error: can\'t find file or read data")
        return
   content = infile.readlines() #store the lines in a list
   try:
        assert lineNumber>=0 #ensure that the line  is not a negative value
        assert n>=0 #ensure that the number of duplicates  is not a negative value
        for i in range(n):
            content.insert(int(lineNumber)+1,content[lineNumber]) #insert n dulicates after this line
   except AssertionError :
        print ("Error: can't have a negative number")# ensure no negatives
        
   except IndexError: # ensuring that no boundaries are out
        print("Line is out of bound there are only "+str(len(content))+" lines in this file and it is 0 indexed so choose from 0 to "+str(len(content)-1))
        
   infile.close()  
   infile = open(fileName, 'w') #open in write mode
   infile.write(''.join(content))# write content
   infile.close()



duplicateLine('5.txt',12,4) #here filname is 5.txt followed by linenumber and number of times creates n new duplicates of lineNumber (0 indexed) right after this line. 
