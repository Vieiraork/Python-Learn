v1 = 0
lista = []
matriz = []
line = 30

for i in range(1, 3):
    for v in range(1, 3):
        v1 = int(input(f'Digite o valor [{i}][{v}]: '))
        lista.append(v1)
    matriz.append(lista[:])
    lista.clear()

print(f'-' * line)
print('Matriz gerada')

for i in range(1, 3):
    for v in range(1, 3):
        print(f'[ {matriz[i-1][v-1]} ] ', end='')
    print()

det = (matriz[0][0] * matriz[1][1]) - (matriz[1][0] * matriz[0][1])

print(f'-' * line)
print(f'O valor do determinante é {det}')
