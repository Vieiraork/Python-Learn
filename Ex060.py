numero = int(input('Digite um número: '))

fatorial = 1
i = 1

while i <= numero:
    fatorial *= i
    print('{} * {} = {}'.format(fatorial, i, fatorial))
    i += 1

print('-=-' * 10)
print('O valor de {}! é = {}'.format(numero, fatorial))
