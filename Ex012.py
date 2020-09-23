preco = float(input('Digite o preço do produto: '))
pag = input('Digite V para á vista, P para á prazo ou C para cartão: ')

if pag == 'V' or pag == 'v':
    print('O valor do produto á vista é {}'.format(preco-preco*0.15))
elif pag == 'P' or pag == 'p':
    print('O valor do produto á prazo é {}'.format(preco+preco*0.05))
elif pag == 'C' or pag == 'c':
    print('O valor do produto no cartão é {}'.format(preco+preco*0.10))
else:
    print('Por favor, digite uma forma de pagamento válida!')
