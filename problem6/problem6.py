__author__ = 'Jeremy'


f = open("numbers.txt","r")
sum = 0
count = 0
for l in f:
	sum += int(l)
	count += 1
average = sum / count