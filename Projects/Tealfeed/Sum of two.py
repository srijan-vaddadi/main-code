a = input('Enter a list of numbers: ').split()
b = input('Enter a list of numbers: ').split()
v = int(input('Enter a number: '))
x = 0

for i in a:
    a[x] = int(i)
    x += 1

x = 0

for i in b:
    b[x] = int(i)
    x += 1


def sumOfTwo(a, b, v):
    for i in a:
        for j in b:
            if i + j == v:
                return True
    return False


print(sumOfTwo(a, b, v))
