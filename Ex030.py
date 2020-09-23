cores = {'Branco': '\033[1:30m', 'Verde': '\033[1:32m', 'Amarelo': '\033[1:33m'}

numero = int(input('{}Digite um número qualquer: '.format(cores['Branco'])))

if numero % 2 == 0:
    print('O valor {}{}{} é par'.format(cores['Amarelo'], numero, cores['Branco']))
else:
    print('O valor {}{}{} é impar!'.format(cores['Verde'], numero, cores['Branco']))
