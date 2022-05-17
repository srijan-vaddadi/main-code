numb_digit = int(input('Enter in the number of digits: '))
numb = input('Enter the number: ')
max_digit = 0
max_digit_value = 0

for z in range(0, 10):
    z = str(z)
    if max_digit_value < numb.count(z):
        max_digit_value = numb.count(z)
        max_digit = z
    elif z != max_digit and max_digit_value == numb.count(z):
        print('Data was multimodal')
