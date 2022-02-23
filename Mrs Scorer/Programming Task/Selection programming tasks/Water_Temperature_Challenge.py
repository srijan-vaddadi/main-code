x = int(input('water temperature: '))

if x <= 0:
    print('The water is frozen')
elif 0 < x < 100:
    print('The water is liquid')
else:
    print('The water is boiling')
