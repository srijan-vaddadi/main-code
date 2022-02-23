x = float(input('Nitrate level between 1 and 50: '))

if x > 10:
    print('Dose 3ml')
else:
    if x > 2.5:
        print('Dose 2ml')
    else:
        if x > 1:
            print('Dose 1ml')
        else:
            print('Dose 0.5ml')
