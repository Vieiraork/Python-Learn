from time import sleep
from random import randint

lista = []
jogos = []
cont = 1

print(f'{"":-^40}')
print(f'{"MEGA SENA":^40}')
print(f'{"":-^40}')

qtd = int(input('Digite quantos jogos deseja fazer: '))

for i in range(qtd):
    while len(lista) < 6:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
    jogos.append(lista[:])
    lista.clear()

print(f'{"Resultados":^40}')
print(f'{"":-^40}')

for i in jogos:
    print(f'Jogo {cont}: {i}')
    print(f'{"":-^40}')
    sleep(1)
    cont += 1
print(f'{"Boa sorte":^40}')
