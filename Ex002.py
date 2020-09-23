nome = input('Digite seu nome: ')
sexo = input('Digite a primeira letra correspondente ao seu sexo(m ou f): ')

if sexo == 'm' or sexo == 'M':
    print('Seja bem vindo {}'.format(nome))
elif sexo == 'f' or sexo == 'F':
    print('Seja bem vinda {}'.format(nome))
else:
    print('Por favor digite somente M ou F para sexo')
