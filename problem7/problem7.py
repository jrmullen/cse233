__author__ = 'Jeremy'

# import the random module
import random
# define the main function
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