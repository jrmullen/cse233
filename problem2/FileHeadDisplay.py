# -*- coding: utf-8 -*-
#Author Stephen Weatherly
"""Write a program that asks the user for the name of a file. The program should display only
the first five lines of the file’s contents. If the file contains less than five lines, it should
display the file’s entire contents."""

def main():
	#read user selected file
	file1 = open(str(raw_input("Which File: ")),'r')
	#read first line in file
	line = file1.readline()
	count = 0
	#loop until 5 lines are not read or
	#number of lines in the file is less than 5
	while line !='' and count < 5:
		print(line)
		line = file1.readline()
		count = count+1
	file1.close()

main()
