# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 20:45:13 2019

@author: marie
"""

def replaceLine(filename,lineNumber,newString):
    'filename is the name of the file to be manipulated, lineNumber is the lineNumber that will be replaced (0 indexed),newString is the string that will replace the line at lineNumber'
    try:
        infile = open(filename)# open file if not found generate an exception
    except IOError:
        print ("Error: can\'t find file or read data")
        return
    content = infile.readlines()# raed lines and store them in a list
    try:

        content[lineNumber]=newString # the new string will be replace here as the newContent
        assert lineNumber>=0 #ensure that line number is not negative
    except AssertionError :
        print ("Error: can't ahve a negative line number")

    except IndexError:
        print("Line is out of bound there are only "+str(len(content))+" lines in this file and it is 0 indexed so choose from 0 to "+str(len(content)-1))

        
    infile.close()
    
    infile = open(filename, 'w') #open the file as write to amend data 
    infile.write(''.join(content))# write the updated data
    infile.close()#close for better os performane


replaceLine('sample.txt',12,'new string here'+'\n')# here filenname for this question is sample and then linenumber, and the new string you want to add +\n because it si a new line
       
                