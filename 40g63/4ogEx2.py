hours =int(input('Enter the number of hours worked:'))
hourly =int(input('Enter the hourly pay reat:'))
over = (hours - 40) *1.5
time = hourly * 40
if hours > 40: 
    print('\nThe gross pay is ',over*hourly+time)
else:
    print ('The gross pay is ',hours*hourly)
    