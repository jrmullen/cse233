__author__ = 'Jeremy'


def main():

    try:
        golf_file = open('golf.dat', 'r')
        line_num = 0
        for line in golf_file.readlines():
            if (line_num % 2 == 0):
                print('Player name: ' + line)
            else:
                print('Player score: ' + line)
            line_num += 1
        golf_file.close()
        print('Done')
    except IOError:
        print('An error occurred while trying to read information from file.')
    except:
        print('An error has occurred.')
main()