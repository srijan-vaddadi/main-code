import random

for i in range(0,1000000):
    i = i + random.uniform(-0.05,0.05)

x=1

while x>0:
    print(round(i,4))

def trucate(n):
    n = str(n)
    