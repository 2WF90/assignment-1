from src.integer import Integer
from src.multiplication import multiplication_primary, multiplication_karatsuba

#x = Integer([9, 2], False, 12)
#y = Integer([9, 3], True, 12)
x = Integer([5, 4], False, 10)
y = Integer([2, 3], False, 10)

result = multiplication_primary(x, y)

print(result.exponents)