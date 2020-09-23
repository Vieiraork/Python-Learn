opcao = ''
numero = 0
soma = 0
quantidade = 0
menor = 0
maior = 0

while opcao != 'N':
    numero = int(input('Digite um número: '))
    opcao = str(input('Quer continuar? (S/N): ')).upper().strip()

    if opcao != 'N':
        if quantidade == 0:
            maior = numero
            menor = numero

        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

        soma += numero
        quantidade += 1

print('A média entre todos os valores é {:.2f}.'.format(soma/quantidade))
print('O maior valor lido é {}.'.format(maior))
print('O menor valor lido é {}.'.format(menor))
