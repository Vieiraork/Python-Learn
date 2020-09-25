from time import sleep
numero = soma = quantidade = 0

numero = int(input('Digite um número [999 para parar]: '))

while numero != 999:
    soma += numero
    quantidade += 1
    numero = int(input('Digite um número [999 para parar]: '))

print('\033[1;30m')
print('Parando o programa, aguarde...')
sleep(1)
print('A quantidade de números digitados é {} e a soma vale {}'.format(quantidade, soma))
