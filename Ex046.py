from time import sleep

cor = {'Branco': '\033[1;30m', 'Amarelo': '\033[1;33m', 'Default': '\033[m'}

print('-=-' * 20)
print('Contagem para os fogos de artifício do ano novo.')
print('-=-' * 20)
# Laço de repetição controlado, aula12
for i in range(10, 0, -1):
    if i % 2 == 0:
        print('{}Contagem regressiva {}s'.format(cor['Branco'], i))
    else:
        print('{}Contagem regressiva {}s'.format(cor['Amarelo'], i))
    sleep(1)
print('{}Feliz ano novo!'.format(cor['Default']))
