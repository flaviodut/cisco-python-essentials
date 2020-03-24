import math

try:
    x = float(input("Enter a number: "))
    assert x >= 0.0
except AssertionError:
    print('Ops')

x = math.sqrt(x)

print(x)
