x = int(input('number between 1 and 12: '))
times_table = range(1, 13)

for y in times_table:
    print(str(x) + ' x ' + str(y) + ' = ' + str(x*y))
