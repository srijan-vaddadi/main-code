x=5
def access_only():
    return x
def modify():
    x = 'modified'
    return x
def create_locally():
    x = 'local!'
    return x
print(access_only())
print(modify())
print(create_locally())