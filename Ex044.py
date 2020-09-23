preco = float(input('Digite o valor do produto: '))
print('''
 ========== Opções de pagamento ==========
    1 em dinheiro ou cheque 
    2 à vista no cartão 
    3 em 2x no cartão 
    4 em 3x ou mais vezes no cartão
    ''')
pagamento = int(input('Digite a opção de pagamento: '))

if pagamento == 1:
    valor = preco - (preco * 0.10)
    print('O valor do produto à vista é R${:.2f}'.format(valor))
elif pagamento == 2:
    valor = preco - (preco * 0.05)
    print('O valor do produto à vista no cartão é {:.2f}'.format(valor))
elif pagamento == 3:
    parcela = preco / 2
    print('O valor da sua compra é {:.2f} e o valor da sua parcela será {:.2f}'.format(preco, parcela))
elif pagamento == 4:
    valor = preco + (preco * 0.20)
    vezes = int(input('Digite a quantidade de vezes que será dividido o produto: '))

    while(vezes < 3):
        vezes = int(input('Digite a quantidade de vezes que será dividido o produto: '))

    parcela = valor / vezes
    print('O valor do produto R${:.2f}, a quantidade de parcelas é {}x e o valor de cada parcela é R${:.2f}'
          .format(valor, vezes, parcela))
