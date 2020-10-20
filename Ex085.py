numeros = []
par = []
impar = []


for i in range(1, 8):
    n = int(input(f'Digite o {i}º número: '))

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

par.sort()
impar.sort()
numeros.append(par)
numeros.append(impar)

print('-' * 40)
print(f'A lista dos pares {numeros[0]}')
print(f'A lista dos ímpares {numeros[1]}')
