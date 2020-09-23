nome = input('Digite seu nome: ')
sexo = input('Digite somente as iniciais do seu sexo(M/F): ')
azul = '\033[1;34m'
amarelo = '\033[1;33m'

if sexo=='M' or sexo=='m':
    print('{}Olá {}, seja muito bem vindo!'.format(azul, nome))
elif sexo=='F' or sexo=='f':
    print('{}Olá {}, seja muito bem vinda!'.format(amarelo, nome))