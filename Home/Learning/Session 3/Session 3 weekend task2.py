value = float(input('Enter value of goods: '))
print('Value of the good is £' + str(value))
if value >= 200:
    print('You have received a 10% discount')
    print('You now need to pay £' + str(value*0.9))
if 100 <= value <= 199.99:
    print('You have received a 5% discount')
    print('You now need to pay £' + str(round((value*0.95),5)))
