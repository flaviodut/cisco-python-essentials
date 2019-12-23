# 0 == False
# 1 == True

counter_par = 0
counter_impar = 0

number = int(input('Digite um número: '))

# while number != 0 (False)
while number:
    # se divisivel por 0, irá retornar 0
    if number % 2:
        counter_impar += 1
    else:
        counter_par += 1

    print('(Pares:', counter_par, ' / Impar: ', counter_impar, ')')

    number = int(input('Digite um número: '))

print('Finaliza.')