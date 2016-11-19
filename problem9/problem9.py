__author__ = 'Jeremy'


def main():
    try:
        random_numbers = open('numbers1.txt', 'r')
        number = 0
        total = 0
        average = 0
        print("List of numbers:")
        for line in random_numbers.readlines():
              print(line)
              total = total+int(line)
              number +=1
        average = total/number
        print("Sum of all numbers = " + str(total))
        print("Lines read: " + str(number))
        print("Average: " + str(average))
    except(IOError, ValueError):
        pass
main()