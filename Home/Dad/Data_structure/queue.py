import random
''''# Python program to
# demonstrate queue implementation
# using list

# Initializing a queue
queue = ['a', 'b', 'c']

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty
'''

orders = []
ctr = 0


def food_done(x):
    y = x
    ctr2 = 0
    for food in y:
        y.pop(0)
        ctr2 += 1
        print(ctr2)
    print('Customer', str(ctr), 'food is ready')


for customer in range(1, 6):
    order_numb = random.randint(1, 4)
    order_append = []
    for i in range(1, order_numb + 1):
        order_append.append(i)
    orders.append(order_append)

print(orders)

for customer in orders:
    ctr += 1
    food_done(customer)

# TypeError: list indices must be integers or slices, not list
# 31, 43
