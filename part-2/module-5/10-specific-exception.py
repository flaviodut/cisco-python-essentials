try:
    x = int(input('Bota um número: '))
    y = 1 / x
    print(y)
except (ZeroDivisionError, ValueError):
    print('Deu ruim, truta.')
except:
    print('Pipoco padrão.')

print('Fim.')
