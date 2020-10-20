matriz = []
lista = []

for li in range(3):
    for co in range(3):
        n = int(input(f'Digite o valor para a matriz[{li}][{co}]: '))
        lista.append(n)
    matriz.append(lista[:])
    lista.clear()

for li in range(3):
    for co in range(3):
        print('[ {:^5} ] '.format(matriz[li][co]), end='')
    print('')
