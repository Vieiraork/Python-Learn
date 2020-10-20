lista = []
matriz = []
primeira = []
segunda = []
res = []

for li in range(3):
    for co in range(3):
        n = int(input(f'Digite o valor da matriz[{li}][{co}]: '))
        lista.append(n)
        if co == 0:
            primeira.append(n)
        if co == 1:
            segunda.append(n)
    matriz.append(lista[:])
    lista.clear()

matriz[0].append(primeira[0])
matriz[0].append(segunda[0])

matriz[1].append(primeira[1])
matriz[1].append(segunda[1])

matriz[2].append(primeira[2])
matriz[2].append(segunda[2])

print('*' * 50)

for li in range(3):
    for co in range(5):
        print('[ {:^5} ] '.format(matriz[li][co]), end='')
    print('')
print('*' * 50)

res.append(matriz[0][0] * matriz[1][1] * matriz[2][2])
res.append(matriz[0][1] * matriz[1][2] * matriz[2][3])
res.append(matriz[0][2] * matriz[1][3] * matriz[2][4])

res.append(matriz[0][2] * matriz[1][1] * matriz[2][0])
res.append(matriz[0][3] * matriz[1][2] * matriz[2][1])
res.append(matriz[0][4] * matriz[1][3] * matriz[2][2])

det = (res[0] + res[1] + res[2]) - (res[3] + res[4] + res[5])

print(f'O determinante da matriz vale: {det}')
