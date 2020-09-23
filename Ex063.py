print('-=-' * 30)
print('Sequência de Fibonacci')
print('-=-' * 30)
cont = 3
soma = 0
anterior = 0

numero = int(input('Quantos números você deseja exibir? '))
lista = [0, 1]

soma = lista[0] + lista[1]
lista.append(soma)

print('{} -> {} -> {} '.format(lista[0], lista[1], soma), end='')
soma = lista[1] + lista[2]
lista.append(soma)

while cont <= numero:
    print('-> {} '.format(soma), end='')
    anterior = cont - 1

    soma += lista[anterior]
    lista.append(soma)

    cont += 1
print('Fim')
