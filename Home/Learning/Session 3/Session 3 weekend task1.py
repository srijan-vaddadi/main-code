import random

die1 = random.randint(1,6)
die2 = random.randint(1,6)

if die1 == die2:
    print('You threw a double')
    print((die1+die2)*2)
else:
    print(die1+die2)