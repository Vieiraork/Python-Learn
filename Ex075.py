numeros = (int(input('Digite o primeiro número: ')),
           int(input('Digite o segundo número: ')),
           int(input('Digite o terceiro número: ')),
           int(input('Digite o quarto número: ')))
print('-=-' * 20)
print(f'Você digitou os números {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)}ª posição')
print('Quais são os números pares: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'{n}')

