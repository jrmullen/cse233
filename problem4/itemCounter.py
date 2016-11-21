# -*- coding: utf-8 -*-
#Stephen Weatherly
"""Assume that a file containing a series of names (as strings) 
is named names.txt and exists on the computer’s disk. Write a 
program that displays the number of names that are storedin the 
file. (Hint: Open the file and read every string stored in it. 
Use a variable to keep a count of the number of items that are 
read from the file.)"""

def main():
	print("Welcome to the Item Counter")
	infile = open('names.txt','r')
	count=0
	for line in infile:
		count +=1
		print(line.rstrip('\n'))
	print "Total Names: ",count
	infile.close()
	
main()
