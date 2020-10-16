lista = []

for i in range(5):
    n = int(input(f'Digite o {i+1}º valor: '))
    if i == 0 or n > lista[len(lista)-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
for p in range(5):
    print(f'{lista[p]} - ', end='')
print('End')
