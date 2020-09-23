frase = str(input('Digite uma frase: ')).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('A primeira frase {} e seu inverso {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo! A palavra {}.'.format(junto))
else:
    print('A frase digitada não é um palíndromo!')
