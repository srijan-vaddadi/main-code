x = int(input('Mark: '))

if 0 <= x < 2:
    print('Grade: U')
    y = 2-x
    print('You need ' + str(y) + ' marks to reach the next grade')
if 2 <= x < 4:
    print('Grade: 1')
    y = 4-x
    print('You need ' + str(y) + ' marks to reach the next grade')
if 4 <= x < 13:
    print('Grade: 2')
    y = 13-x
    print('You need ' + str(y) + ' marks to reach the next grade')
if 13 <= x < 22:
    print('Grade: 3')
    y = 22-x
    print('You need ' + str(y) + ' marks to reach the next grade')
if 22 <= x < 31:
    print('Grade: 4')
    y = 31-x
    print('You need ' + str(y) + ' marks to reach the next grade')
if 31 <= x < 41:
    print('Grade: 5')
    y = 41-x
    print('You need ' + str(y) + ' marks to reach the next grade')
if 41 <= x < 54:
    print('Grade: 6')
    y = 54-x
    print('You need ' + str(y) + ' marks to reach the next grade')
if 54 <= x < 67:
    print('Grade: 7')
    y = 67-x
    print('You need ' + str(y) + ' marks to reach the next grade')
if 67 <= x < 80:
    print('Grade: 8')
    y = 80-x
    print('You need ' + str(y) + ' marks to reach the next grade')
if 80 <= x:
    print('Grade: 9')

# make all elif for time