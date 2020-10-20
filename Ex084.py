pessoas = []
lista = []
total = cont = cont_ = 0
linha = 30

while True:
    nome = input('Digite seu nome: ')
    peso = float(input('Digite seu peso: '))

    lista.append(nome)
    lista.append(peso)
    pessoas.append(lista[:])
    lista.clear()
    total += 1

    op = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    print('-' * linha)
    if op in 'N':
        break

print(f'Foram cadastradas {total} pessoas.')
for pessoa in pessoas:
    if pessoa[1] > 70:
        if cont < 1:
            print('Pessoas pesadas ', end='')
        print(f'{pessoa[0]}, ', end='')
        cont += 1
    else:
        print('\n')
        if cont_ < 1:
            print('Pessoas leves ', end='')
        print(f'{pessoa[0]}, ', end='')
        cont_ += 1
