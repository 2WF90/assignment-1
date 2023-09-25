from src.integer import Integer
from src.multiplication import multiplication

x = Integer([9, 2], False, 12)
y = Integer([9, 3], True, 12)

result = multiplication(x, y)

print(result.exponents)