#import (subtraction, multiplication, devision)

def ModInverse(a: int, modulus: int):
    xOne = 1
    xTwo = 0
    while modulus > 0:
        # q = rounddown(a / m) (Use devision)
        # r = a - q * m (use subtraction and multiplication)
        # a = m
        # m = r
        # xThree = xOne - q * xTwo (use subtraction and multiplication)
        # xOne = xTwo
        # xTwo = xThree
        pass
    
    if a == 1:
        inverse = xOne
        return inverse
    
    return 'inverse does not exist'