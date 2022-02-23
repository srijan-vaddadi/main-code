import random

plaintext = input('Enter a word: ')
# user input
plainlen = len(plaintext)
# length of input
print(plainlen)
randomkey = []
# list for new letters generated
xorletters = []
# list of XORed values 

for char in plaintext:
    ofset = random.randint(1, 26)
    randomascii = ofset + 96
    randomletter = chr(randomascii)
    randomkey.append(randomletter)
    newpos = ord(char) ^ ord(randomletter)
    xorletters.append(newpos)

xorout = []
for num in xorletters:
    lettertoadd = chr(num)
    xorout.append(lettertoadd)

# creates new letters by adding random number to ASCII - 1 of A
# adds it to the list
# XORs the ASCII of each letter of plaintext and randomascii

print(randomkey)
print(xorletters)
print(xorout)
