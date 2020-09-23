from random import randint
from time import sleep

computador = randint(0, 5)
cores = {'Azul': '\033[1:34m', 'Amarelo': '\033[1:33m', 'Verde': '\033[1:32m',
         'Turquesa': '\033[1:36m', 'Braco': '\033[1:30m', 'Vermelho': '\033[1:31m'}

print('{}-=-'.format(cores['Azul']) * 15)
print('{}Pensando em um número, tente adivinhar...'.format(cores['Braco']))
print('{}-=-'.format(cores['Azul']) * 15)

jogador = int(input('{}Digite um número entre 0 e 5: '.format(cores['Braco'])))

print('Processando...')
sleep(2)

if jogador == computador:
    print('{}Você acertou o número, seu número {} o número sorteado {}'
          .format(cores['Verde'], jogador, computador))
else:
    print('{}Você não acertou o número sorteado, seu número {} o número sorteado {}'
          .format(cores['Vermelho'], jogador, computador))
