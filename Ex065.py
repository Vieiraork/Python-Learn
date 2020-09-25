opcao = ''
numero = soma = quantidade = menor = maior = 0

while opcao in 'S':
    numero = int(input('Digite um número: '))
    opcao = str(input('Quer continuar? (S/N): ')).upper().strip()

    soma += numero
    quantidade += 1

    if quantidade == 1:
        maior = numero
        menor = numero

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print('Foram lidos {} numeros'.format(quantidade))
print('A média entre todos os valores é {:.2f}.'.format(soma/quantidade))
print('O maior valor lido é {}.'.format(maior))
print('O menor valor lido é {}.'.format(menor))
