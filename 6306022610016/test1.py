
men = int(input('Input number of male students : '))
women = int(input('Input number of female students : '))
total = men + women
print('There are',(total),'students with ', \
    format(men/total*100,(',.2f')),' male and ',\
        format(women/total*100,(',.2f')),' female ', sep='')