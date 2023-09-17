from functools import wraps
from decorators import callonce

#----------------------------------------------------------------
# DEFINITION TYPE INTR
#----------------------------------------------------------------

# Modified version of: https://stackoverflow.com/questions/23709429/how-to-emulate-4-bit-integer-in-python-3
# IntR represents a single digit of radix t
# IntR is a subclass of int, therefore all standard operations that apply to int also apply to IntR
# param t: the radix of IntR (functions as the type of the object)
# param val: the value of the number 
class IntR(int):
    def __new__(self, r, val):
        initIntR()
        self.r = r
        return super(IntR, self).__new__(self, val & r)
    
    def radix(self):
        return self.r

#----------------------------------------------------------------
# INITIALIZATION OF INTR
#----------------------------------------------------------------

# Makes sure that after performing an operation all the types are set correctly (including radix)
def add_special_method(cls, name):
    mname = '__{}__'.format(name)
    @wraps(getattr(cls, mname))
    def convert_to_cls(self, other):
        bound_original = getattr(super(cls, self), mname)
        return type(self)(r=self.radix(), val=bound_original(other))
    setattr(cls, mname, convert_to_cls)

# Iterates over all standerd int operations and makes sure they also apply to IntR
# This should only run once
@callonce
def initIntR():
    for m in ('add', 'sub', 'mul', 'floordiv', 'mod', 'pow',
            'lshift', 'rshift', 'and', 'xor', 'or'):
        add_special_method(IntR, m)
        add_special_method(IntR, 'r' + m)  # reverse operation

# testing
if __name__ == "__main__":
    x = 4
    y = 15
    u = IntR(0xf, x)
    v = IntR(0xf, y)

    print(bin(x * y))
    print((x * y) & 0xf)
    print( v % u)
    print(u*v)
    from operator import * 
    print(mul(u, v))
    print(type(u + y))