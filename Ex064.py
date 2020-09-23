numero = 0
soma = 0
quantidade = 0

while numero != 999:
    numero = int(input('Digite um número: '))

    if numero != 999:
        soma += numero
        quantidade += 1
print('A quantidade de números digitados é {} e a soma vale {}'.format(quantidade, soma))
