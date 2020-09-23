termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
i = 1

while i < 11:
    print('{} -> '.format(termo), end=' ')
    termo += razao
    i += 1

print('Fim')
