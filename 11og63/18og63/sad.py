first = input('Enter your first name :')
last = input('Enter your last name :')
number = input('Enter your student ID number :')
a = first[:3]+last[:3]+number[-3:]

print('Your system login name is :',a)