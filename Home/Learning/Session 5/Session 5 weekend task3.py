name = 'something'
mainList = []

name = input('Enter name: ')
age = input('Enter age: ')
year_of_birth = input('Year of birth: ')
mainList.append([name, age, year_of_birth])

while name != 'stop':
    name = input('Enter name: ')
    if name == 'stop':
        break
    else:
        age = int(input('Enter age: '))
        year_of_birth = input('Year of birth: ')
        mainList.append([name, age, year_of_birth])

print(mainList)
