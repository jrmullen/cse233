__author__ = 'Jeremy'

def main():
    try:
        golf_scores = int(input('Number of players: '))
        golf_file = open('golf.dat', 'w')
        for count in range(1, golf_scores + 1):
            print('Enter the name and score for player #' + str(count))
            name = input('Name: ')
            score = int(input('Score: '))

            golf_file.write(name + '\n')
            golf_file.write(str(score) + '\n')
        print()
        golf_file.close()
        print('Done')
    except IOError:
        print('An error occurred trying to write information to file.')
    except ValueError:
        print('Player\'s score must be an integer')
    except:
        print('An error has occurred.')

main()