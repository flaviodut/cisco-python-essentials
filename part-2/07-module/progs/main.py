from sys import path

path.append('/Users/flaviodutra/Documents/Web/Studies/cisco-python-essentials/part-2/07-module/modules/')

import mymodule

zeroes = [4 for i in range(5)]
ones = [2 for i in range(5)]

print(mymodule.suml(zeroes))
print(mymodule.prodl(ones))
