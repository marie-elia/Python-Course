# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 00:41:41 2019

@author: marie
"""

def deleteLine(filename,lineNumber):
    'deletes the line numbered at lineNumber from fileName (0 indexed)'
    try:
        infile = open(filename)# open the file if not found generate exception
    except IOError:
        print ("Error: can\'t find file or read data")
        return  
    
    content = infile.readlines() #store the lines in a list
    try:

        del content[lineNumber] # delete the line 
        assert lineNumber>=0 #ensure that the line  is not a neagtive value
    except AssertionError :
        print ("Error: can't have a negative line number")
        return
    except IndexError:
        print("Line is out of bound there are only "+str(len(content))+" lines in this file and it is 0 indexed so choose from 0 to "+str(len(content)-1))
        return
    infile.close()
    
    infile = open(filename, 'w') #open the file as write to amend data 
    infile.write(''.join(content))# write the updated data
    infile.close()#close for better os performane



deleteLine('2.txt',7)# here filenname for this question is sample and then linenumber