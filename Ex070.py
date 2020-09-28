total = mil = menor = cont = 0
barato = ''

while True:
    produto = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o valor do produto: R$'))

    total += preco
    cont += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    if preco > 1000:
        mil += 1

    continar = ' '
    while continar not in 'SN':
        continar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    print('-=-' * 20)
    if continar in 'N':
        break

print('A lista de produtos conta com {} intens e o valor da compra é R${:.2f}'.format(cont, total))
print('{} produto(s) custa(m) acima de R$1000,00'.format(mil))
print('{} é o nome do produto mais barato e custa R${}'.format(barato, menor))
