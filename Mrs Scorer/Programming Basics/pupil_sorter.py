pupil_even = []
pupil_odd = []

for i in range(0, 20):
    pupil_name = input('Enter a name: ')
    if i%2 == 0:
        pupil_even.append(pupil_name)
    else:
        pupil_odd.append(pupil_name)

print(pupil_odd)
print(pupil_even)
