palavra = str(input('Digite algo: ')).strip()

print('A quantidade de vezes que a letra A aparece é {}'.format(palavra.upper().count('A')))

print('A primeira letra A apareceu na posição {}'.format(palavra.upper().find('A') + 1))
print('A ultima letra A apareceu na posição {}'.format(palavra.upper().rfind('A')))
