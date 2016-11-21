# -*- coding: utf-8 -*-
#Author Stephen Weatherly
"""Write a program that asks the user for the name of a file. 
The program should display the contents of the file with each 
line preceded with a line number followed by a colon. The line 
numbering should start at 1"""
def main():
	print("Line Numbers")
	fname = raw_input("Enter file name: ")
	infile = open(fname,'r')
	count = 0
	#loop to read each line
	for line in infile:
		count +=1
		#concat line number and colon
		print count,':',line.rstrip()
	infile.close()
	
main()
