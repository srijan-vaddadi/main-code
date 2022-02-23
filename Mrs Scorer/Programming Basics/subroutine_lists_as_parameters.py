bar = ['a','b','c']
def foo(x):
    x[0] = 25
    x = [1,2,3]
    print(x)
foo(bar)
print(bar)

