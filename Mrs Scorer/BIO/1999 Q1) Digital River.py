x = input("value n where n is between 1 and 16384: ")

y = 0

def addon(x):
    while y <= len(x):
        sum1 = int(x[y])
        y = y+1
    while y <= len(x):
        sum2 = int(x[y])
        y = y+1
    while y <= len(x):
        sum3 = int(x[y])
        y = y + 1
    while y <= len(x):
        sum4 = int(x[y])
        y = y+1
    while y <= len(x):
        sum5 = int(x[y])
    sum_total = sum1+sum2+sum3+sum4+sum5
    print(sum_total)

addon()