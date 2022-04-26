number = 0
while number < 1 or number > 10:
    number = int(input('Enter a positive number: '))
    if number > 10:
        print('number is too large')
    else:
        if number < 1:
            print('number is not positive')

c = 1
for k in range(1, number):
    print(c)
    c = (c*(number - 1 - k))//(k + 1)


'''def LoadGreyScaleImage(ImageTitle):
    global key
    key = int(ImageTitle[len(ImageTitle) - 1])
    return key


def FindSecretChar(PixelValue):
    s_numb = PixelValue - key
    if 0 < s_numb <= 26:
        s_ascii = s_numb + 96
        s_char = chr(s_ascii)
    elif s_numb == 0:
        s_char = ' '
    else:
        s_char = '_'
    return s_char


LoadGreyScaleImage('image5')
print(FindSecretChar(27))
'''


