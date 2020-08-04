print ('Please select operation')
print ('1. Add \n2. Subtract \n3. Multiply \n4. Divide')
num = int(input('Select operations from 1,2,3,4 :'))
first = int(input('Enter first number :'))
second = int(input('Enter second number :'))
if num == 1 :
    print (">>",first,'+',second,"=",(first+second))
elif num == 2 :
    print (">>",first,'-',second,"=",(first-second))
elif num == 3 :
    print (">>",first,'*',second,"=",(first*second))
elif num == 4 : 
    print (">>",first,'/',second,"=",(first/second))
