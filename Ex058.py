from random import randint
contador = 0
computador = randint(0, 10)

def mensagem():
    print('Aqui quem fala é seu computador e acabei de pensar em um número de 0 à 10...')
    print('Será que você consegue advinhar?')


jogador = int(input('Digite um número entre 0 e 10: '))
mensagem()

while computador != jogador:
    jogador = int(input('Digite novamente um número de 0 até 10: '))
    computador = randint(0, 10)
    if computador != jogador:
        contador += 1
print('A quantidade de vezes necessária para o jogador sair foi {} vez(es)'.format(contador))
