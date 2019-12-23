largest_number = -999999

number = int(input('Digite um número: '))

while number != -1:
    if number > largest_number:
        largest_number = number;
        print('Maior número atualizado.')
    else:
        print('Número digitado não é maior que o anterior.')

    print('Maior número:', largest_number)

    number = int(input('Digite um número: '))

print('Finaliza.')