multiplicacao = 0
while True:
    numero = int(input('Digite um número [numero negativo para sair]: '))
    print('-=-' * 20)

    if numero < 0:
        break
    print(f'Tabuada de {numero} é:')

    for tabuada in range(1, 11):
        multiplicacao = tabuada * numero
        print(f'{numero} x {tabuada:2} = {multiplicacao}')
    print('-=-' * 20)
print('\033[1;30m')
print('Obrigado por testar nosso programa, volte sempre!')
