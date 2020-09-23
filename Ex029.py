cores = {'Branco': '\033[1:30m', 'Vermelho': '\033[1:31m', 'Verde': '\033[1:32m',
         'Amarelo': '\033[1:33m'}

velocidade = int(input('{}Digite a sua velocidade na estrada: '.format(cores['Branco'])))

if velocidade > 0:
    if velocidade > 80:
        valor = (velocidade - 80) * 7.00
        print('{}Você foi multado e o valor que irá pagar é de {}R${}'
              .format(cores['Vermelho'], cores['Amarelo'], valor))
    else:
        print('{}Você estava dentro da velocidade permitida pela via, parabéns continue assim!'
              .format(cores['Verde']))
else:
    print('{}Digite valores numericos positivos para velocidade'.format(cores['Vermelho']))
