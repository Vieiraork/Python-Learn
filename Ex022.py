frase = input('Digite seu nome completo: ').strip()

print('Nome com as letras maiusculas: {}'.format(frase.upper()))
print('Nome com as letras minusculas: {}'.format(frase.lower()))
print('Quantidade de caracteres sem considerar espaços é {}'.format(len(frase)-frase.count(' ')))

primeiro = frase.split()[0]

print('Seu primeiro nome é {} e pussui {} letras'.format(primeiro, len(primeiro)))
# A contagem de letras do primeiro nome pode ser feito frase.find(' ')
