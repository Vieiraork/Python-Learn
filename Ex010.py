real = float(input('Digite o valor em R$: '))

dolar = real / 5.59
euro = real / 6.60

print('Com R${:.2f} você pode comprar US${:.2f}.'.format(real, dolar))
print('Com R${:.2f} você pode compara €{:.2f}'.format(real, euro))