import random
from time import sleep

#Função de espera antes do jogo começar
def espera():
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')

#Função para o menu
def menu():
    print('''Entre com somente as opções disponíveis:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
    ''')


# Imprime 15 vezes a sequência de string
print('-=-' * 15)
print('Olá jogador, pronto para esse desafio? ')
print('-=-' * 15)

menu()
jogador = int(input('Digite uma das opções: ')) # Recebe a entrade das opções do jogador
opcoes = ('Pedra', 'Papel', 'Tesoura') # As opções de palavras disponíveis para o funcionamento do jogo
computador = random.randint(0, 2) # Randomizador para que o computador 'jogue'

espera()# Função de espera antes do jogo começar
# Estrutura condicional para decidir o vencedor
if jogador >= 0 and jogador < 3:
    if computador == 0:
        if jogador == 0:
            print('Computador {} Jogador(a) {}, EMPATE!'.format(opcoes[computador], opcoes[jogador]))
        elif jogador == 1:
            print('Computador {} Jogador(a) {}, JOGADOR GANHOU!'.format(opcoes[computador], opcoes[jogador]))
        elif jogador == 2:
            print('Computador {} Jogador(a) {}, COMPUTADOR GANHOU!'.format(opcoes[computador], opcoes[jogador]))
    elif computador == 1:
        if jogador == 0:
            print('Computador {} Jogador(a) {}, COMPUTADOR GANHOU!'.format(opcoes[computador], opcoes[jogador]))
        elif jogador == 1:
            print('Computador {} Jogador(a) {}, EMPATE!'.format(opcoes[computador], opcoes[jogador]))
        elif jogador == 2:
            print('Computador {} Jogador(a) {}, JOGADOR GANHOU!'.format(opcoes[computador], opcoes[jogador]))
    elif computador == 2:
        if jogador == 0:
            print('Computador {} Jogador(a) {}, JOGADOR GANHOU!'.format(opcoes[computador], opcoes[jogador]))
        elif jogador == 1:
            print('Computador {} Jogador(a) {}, COMPUTADOR GANHOU!'.format(opcoes[computador], opcoes[jogador]))
        elif jogador == 2:
            print('Computador {} Jogador(a) {}, EMPATE!'.format(opcoes[computador], opcoes[jogador]))
else:
    print('Por favor digite somente uma das opções informadas no menu!')
