lista = []
opcao = ''

while True:
    numero = int(input('Digite um número: '))

    if numero in lista:
        print('Valor duplicado, tente novamente.')
    else:
        lista.append(numero)
        print(f'O valor inserido é {numero}')

    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while opcao not in 'NS':
        opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if opcao in 'N':
            break
    if opcao in 'N':
        break
    print(f'{"-":-^40}')

print(f'Os valores digitados na lista são {lista}')
