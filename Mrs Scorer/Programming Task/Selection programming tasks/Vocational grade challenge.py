x = int(input('Test Mark: '))
if x < 40:
    print('FAIL')
elif 40 <= x < 60:
    print('PASS')
elif 60 <= x < 80:
    print('MERIT')
elif 80 <= x <= 100:
    print('DISTINCTION')

