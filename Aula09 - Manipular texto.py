frase = 'Curso em Vídeo Python'
nome = 'William Vieira Brito da Silva'


# Fatiamento de String
print(frase[9:])
print(frase[::2])
print(len(nome))
espaços = nome.count(' ')
total = len(nome)
soma = total - espaços
print('A quantidade de caracteres sem espaços é {}'.format(soma))

