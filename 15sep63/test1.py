def main():
    bass = 'Y'

    print ('Choose number :')
    print ('1) read ')
    print ('2) write ')

    choice = int(input(' : '))
    while bass == 'Y' or bass == 'y' :
        if choice == 1:
            num_one()
        elif choice == 2:
            num_two()
        else:
            print('Only 1 or 2 ')
        bass = input('Do this again?:(press Y or N)')
        if bass == 'Y' or bass == 'y' :
            print ('Choose number :')
            print ('1) read ')
            print ('2) write ')
            choice = int(input('; '))

def num_one():
    infile = open('15sep63/ine2friends.txt','r')
    file_contents = infile.read()

    infile.close()
    print(file_contents)

def num_two():
    infile = open('15sep63/ine2friends.txt','a')
    name = input('Enter your name :')
    infile.write(name + '\n')

    infile.close()

main()