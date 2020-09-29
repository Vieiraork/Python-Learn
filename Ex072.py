numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    while escolha not in range(0, 21):
        escolha = int(input('Por favor, digite somente o números entre 0 e 20: '))

    print(f'O número digitado foi {numeros[escolha]}.')

    while True:
        continuar = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]

        if continuar in 'SN':
            print('-=-' * 15)
            break

    if continuar in 'N':
        break
print('Programa encerrado, obrigado por utilizar.')
