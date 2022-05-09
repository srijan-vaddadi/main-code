x = input('Enter a string: ').split()
my_list = []
total_numb = 0

for word in x:
    try:
        is_numb = int(word)
        my_list.append(is_numb)
    except:
        pass

for numb in my_list:
    total_numb += numb

print(total_numb)