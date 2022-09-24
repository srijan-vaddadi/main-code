numb_digit = int(input('Enter in the number of digits: '))
numb = input('Enter the number: ')
max_digit = 0
max_digit_count = 0

for z in range(0, 10):
    z = str(z)
    if max_digit_count < numb.count(z):
        max_digit_count = numb.count(z)
        max_digit = z
    elif max_digit_count == numb.count(z) and numb.count(z) != 0:
        print('Data was multimodal')
        break

print(max_digit_count)
