__author__ = 'Jeremy'



f = open("numbers.txt","r")
sum = 0
for l in f:
    sum += int(l)
