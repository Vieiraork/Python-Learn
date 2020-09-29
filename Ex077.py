palavras = ('arroz', 'queijo', 'salada', 'beijo', 'video', 'jogos', 'felicidade')

for vogais in palavras:
    print(f'\nNa palavra {vogais} temos ', end='')
    for letra in vogais:
        if letra in 'aeiou':
            print(letra , end=' ')
