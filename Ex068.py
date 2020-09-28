from random import randint
from time import sleep

soma = cont = 0
jescolha = ''

print('Jogo do PAR ou IMPAR, está pronto caro jogador?')
print('Carregando...')
sleep(1)

while True:
    computador = randint(0, 21)
    jogador = int(input('Digite um número entre 1 e 20: '))
    while jescolha not in 'PI':
        jescolha = str(input('PAR ou IMPAR? [P/I] ')).strip().upper()[0]

    soma = computador + jogador

    if jescolha == 'P' and soma % 2 == 1:
        break
    if jescolha == 'I' and soma % 2 == 0:
        break
    cont += 1

print('Fechando jogo...')
sleep(1)

if cont == 0:
    print('Não foi registrada nenhuma vitoria.')
else:
    print(f'Registramos {cont} vitoria(s) consegutiva(s) do jogador.')
