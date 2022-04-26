number_in = int(input('Enter a positive number: '))
number_out = 0
count = 0

while number_in > 0:
    count += 1
    part_value = number_in % 2
    number_in //= 2

    for i in range(1, count):
        part_value *= 10
    number_out += part_value

print('The result is', str(number_out))
