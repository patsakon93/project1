score = int(input('Enter a tast score: '))

while score < 0 or score > 100:
    print('ERROR: vThe score cannot be negative')
    print('or greater than 100.')
    score = int(input('Enter the correct score: '))