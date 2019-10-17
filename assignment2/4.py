# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 01:18:59 2019

@author: marie
"""

def stripLine(fileName, lineNumber, character):
   'removes character from lineNumber in fileName (0 indexed)'
   try:
        infile = open(fileName)#open file read 
   except IOError:
        print ("Error: can\'t find file or read data")
        return
   content = infile.readlines() #store the lines in a list
   try:
        assert lineNumber>=0 #ensure that the line  is not a neagtive value
        
        content[lineNumber]=content[lineNumber].replace(character,"")# replace a certain character by nothing meaning remove this character frm a certain line

   except AssertionError :
        print ("Error: can't have a negative line number")
        return
   except IndexError:# ensure that no out of bound errors happened
        print("Line is out of bound there are only "+str(len(content))+" lines in this file and it is 0 indexed so choose from 0 to "+str(len(content)-1))
        return
   infile.close()  
   infile = open(fileName, 'w')
   infile.write(''.join(content))#write data to file
   infile.close()



stripLine('4.txt',6,'e')#filename here is 4.txt and linenumber and certain character to be removed 
