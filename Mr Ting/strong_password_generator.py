import random
character_numb = int(input('Enter the number of characters in your password: '))
rand_password = ''
for i in range(character_numb):
    character = random.randint(33, 127)
    rand_character = chr(character)
    rand_password += rand_character
print(rand_password)