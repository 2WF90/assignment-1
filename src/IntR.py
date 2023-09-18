from functools import wraps
from decorators import callonce

#----------------------------------------------------------------
# DEFINITION TYPE INTR
#----------------------------------------------------------------

# Modified version of: https://stackoverflow.com/questions/23709429/how-to-emulate-4-bit-integer-in-python-3
# IntR represents a single digit of radix t
# IntR is a subclass of int, therefore all standard operations that apply to int also apply to IntR
# IntR ONLY WORKS FOR BASES THAT ARE A POWER OF 2 - 1 (think of binary -> 0x1, oct -> 0x7 and hex -> 0xf)
# param t: the radix of IntR (functions as the type of the object)
# param val: the value of the number 
class IntR(int):
    def __new__(self, r, val):
        initIntR()

        if r != (r | (r >> 1)):
            raise ValueError('Radix incorrectly formatted, make sure all bits upto the most significant bit are set to 1')

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
    l = IntR(0xff, -5)
    q = IntR(0xff, 3)
    print(l)
    print(l + q)
    print(bin(l+q))
    print((l + q) >> 4)
    print("lmao", IntR(0xf, 5) + IntR(0xf, 15))
    i = IntR(0xff, 5)
    x = 4
    y = 15
    u = IntR(0xf, x)
    v = IntR(0xf, y)
    m = IntR(0x1f, u)
    print(m.radix())

    print(bin(x * y))
    print(bin((x * y) & 0xf))
    print((v * u)& 9)
    print(u+v)
    from operator import * 
    print(mul(u, v))
    print(type(u + y))