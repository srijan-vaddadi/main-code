x = float(input('Weight: '))
y = input('(K)g or (l)bs: ')

if y.upper() == 'K':
    print('weight in pounds = ' + str(x*2.20462)+'lbs')
elif y.upper() =='L':
    print('weight in kilograms = ' + str(x*0.453592) + 'kg')
