keep_going = 'y'
while keep_going == 'y' or keep_going == 'Y' :
    sales = float(input('Enter thre amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    commission = sales * comm_rate

    print('The commission is $', \
    format(commission, ',.2f'), sep='')

    keep_going = input('Do you want to calculater another' + \
                        'commission (Enter y for yes): ')
