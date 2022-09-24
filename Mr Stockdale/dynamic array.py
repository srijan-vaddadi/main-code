import datetime

print(datetime.datetime.now())
lst = [x for x in range(10000000)]
lst.insert(1, 'a')
print(datetime.datetime.now())
