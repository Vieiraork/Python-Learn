num = int(input('Digite um número: '))

cores = {'White': '\033[1;30m', 'Red': '\033[1;31m', 'Default': '\033[m'}
# Números brancos são primos, números vermelhos não são primos

for i in range(1, num):
    if i % 2 == 0 and i != 2 or i % 3 == 0 and i != 3 or i % 5 == 0 and i != 5 or i % 7 == 0 and i != 7:
        print('{}'.format(cores['Red']), end=' ')
        print('{}'.format(i), end=' ')
    elif i != 1:
        print('{}'.format(cores['White']), end=' ')
        print('{}'.format(i), end=' ')
