# -*- coding: utf-8 -*-
#Author:Stephen Weatherly
"""Assume that a file containing a series of integers is named 
numbers.txt and exists on the computer’s disk. Write a program 
that displays all of the numbers in the file."""

def main():
	#create infile and open txt file in r mode
	infile = open('number.txt','r')
	#read every line from infile
	for line in infile:
		#convert each line into an int
		number = int(line)
		print(number)
	#close file to prevent data loss
	infile.close()
	
main()
