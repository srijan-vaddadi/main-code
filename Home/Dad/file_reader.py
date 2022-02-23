with open('C:/Srijans_stuff/text_files/text_to_read.txt') as f:
    line = f.readlines()
    print('Content of file text_to_read.txt is: ')
    print('##########')
    line_c = 0
    while line:
        print(line + str(line_c))
        line = f.readlines()
        line_c += 1
print('#############')

# print('number of lines')
# print('number of words then letters')
