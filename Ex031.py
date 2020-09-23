km = int(input('Digite a distância até seu ponto de destino: '))

if km > 0:
    if km <= 200:
        preco = km * 0.50
        print('Caro(a) passageiro(a)')
        print('O preço da sua passagem é {}'.format(preco))
    else:
        preco = km * 0.45
        print('Caro(a) passageiro(a)')
        print('O preço da sua passagem é {}'.format(preco))
else:
    print('Digite um valor numerico acima de 0 para distância!')
