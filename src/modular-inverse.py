#import (subtraction, multiplication, devision)
from src.basic_arithmetic import add, subtract

# Computes the modular inverse for a mod m. If it exists.
def ModInverse(a: int, modulus: int):
    xOne = 1
    xTwo = 0
    while modulus > 0:
        # q = rounddown(a / m) #(Use devision, discard rest)

        r = subtract(a, q * m) #(use multiplication)
        a = m
        m = r
        xThree = subtract(xOne, q * xTwo) #(use multiplication)
        xOne = xTwo
        xTwo = xThree
        pass
    
    if a == 1:
        inverse = xOne
        return inverse
    
    return 'inverse does not exist'