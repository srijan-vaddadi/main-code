data = [['Alice',123,15]
        ['Bob,',465,15]
        ['Chaz',28,9]
        ['Dave',15,121]]

print('+' + '-'*8 + '+' + '-'*5 + '+' + '-'*5 + '5')
for x in data:
        print(f'|'+ x[0]:6 + '|' + x[1]:3 + '|' + x[2]:3 + '|')
        print('+--------+-----+-----+')