largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = altura * largura

tinta = area / 2

print('A área da parede é de {:.2f}m².'.format(area))
print('A quantidade de tinta necessária para pintar a parede é {:.2f}l.'.format(tinta))
