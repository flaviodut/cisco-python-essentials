# ValueError
# ImportError

# ZeroDivisionError
# value = 1
# value /= 0

# IndexError
# lst = []
# print(lst[0])

# try/catch from python is try/except
firstNumber = int(input('Escolha um número: '))
secondNumber = int(input('Escolha outro número: '))

try:
    op = firstNumber / secondNumber
    print(op)
except:
    print('Deu ruim, tio.')

print('Fim.')