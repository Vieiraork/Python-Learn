lista = []
matriz = []
somador = somap = maior2 = 0

for li in range(3):
    for co in range(3):
        n = int(input(f'Digite o valor para a matriz [{li}][{co}]: '))
        lista.append(n)
        if n % 2 == 0:
            somap += n
        if li == 1:
            if n > maior2:
                maior2 = n
        if co == 2:
            somador += n
    matriz.append(lista[:])
    lista.clear()

for li in range(3):
    for co in range(3):
        print('[ {:^5} ]'.format(matriz[li][co]), end='')
    print('')

print('*' * 50)
print(f'A soma dos valores pares digitados é: {somap}')
print(f'A soma dos valores da 3ª coluna é: {somador}')
print(f'O maior valor da segunda linha é: {maior2}')
