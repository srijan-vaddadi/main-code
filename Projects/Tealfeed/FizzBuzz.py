numb = int(input('Enter integer: '))

for number in range(1, numb + 1):
    if number % 4 == 0:
        if number % 6 == 0:
            print('FizzBuzz')
            continue
        print('Fizz')
    elif number % 6 == 0:
        print('Buzz')
        continue
    print(number)
