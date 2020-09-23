escolha = int(input('Digite algum número positivo: '))

for i in range(1, 11):
    print('{} x {:2} = {:6}'.format(escolha, i, escolha*i))
