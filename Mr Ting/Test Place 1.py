def parity(i):
    '''parity of integer'''
    b = bin(i)[2:]
    parity = 0
    for digit in b:
        parity ^= int(digit)
    return parity and 'odd'or 'even'

parity(12435)