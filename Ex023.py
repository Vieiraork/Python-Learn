num = int(input('Digite um número: '))

if num >= 0 and num < 9999:
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 100

    print('Unidade: {}'.format(u))
    print('Dezena: {}'.format(d))
    print('Centena {}'.format(c))
    print('Milhar: {}'.format(m))

else:
    print('Digite valores entre 0 e 9999.')


