# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 01:11:37 2019

@author: marie
"""

def swapLines(fileName, lineNumber1, lineNumber2):
    'swaps the lines at lineNumer 1 and 2 in fileName (0 indexed)'
    try:
        infile = open(fileName)# open the file 
    except IOError:
        print ("Error: can\'t find file or read data") # if not found generate exception
        return
    content = infile.readlines()#store the lines in a list
    try:
        
        content[lineNumber1], content[lineNumber2] = content[lineNumber2], content[lineNumber1] # swap the contents of the 2 lines
        assert lineNumber1>=0 #ensure that both lines are not neagtive values
        assert lineNumber2>=0
    except AssertionError :
        print ("Error: can't have a negative line number")
        
    except IndexError: # ensure that no out of bound errors happened
        print("Line is out of bound there are only "+str(len(content))+" lines in this file and it is 0 indexed so choose from 0 to "+str(len(content)-1))
        
    infile.close()
    
    infile = open(fileName, 'w') #open the file as write to amend data 
    infile.write(''.join(content))# write the updated data
    infile.close() # better close file for better os



swapLines('3.txt',3,7)# call the function here, the filename for this question is 3.txt and then the2 linenumbers you want to swap
