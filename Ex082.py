lista = []
par = []
impar = []
c1 = c2 = 0

while True:
    lista.append(int(input('Digite um número: ')))
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    print('-' * 40)
    if opcao in 'N':
        break

for v in lista:
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)

print(f'Os números digitados são {lista}')
print(f'Os números pares digitados são {par}')
print(f'Os números impares digitados são {impar}')
