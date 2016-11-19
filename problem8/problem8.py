__author__ = 'Jeremy'

import random

def main():

    random_numbers = open('random_numbers.txt', 'w')
    num_of_rands =  int(input('How many random numbers should be written to the file?: '))
    print('Numbers written: ')
    for count in range (num_of_rands):
        number = random.randint(1,500)
        print(number)
        random_numbers.write(str(number)+ '\n')
    random_numbers.close()
    print('numbers printed to file')

main()

def main():
        random_numbers = open('random_numbers.txt', 'r')
        number = 0
        total = 0
        print("List of numbers:")
        for line in random_numbers.readlines():
              print(line)
              total = total+int(line)
              number +=1
        print("Sum of all numbers = " + str(total))
        print("Lines read: " + str(number))
main()