num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

print('\nResolução com lista')
lista = [num1, num2, num3]
lista.sort()

print('O menor valor digitado é {}'.format(lista[0]))
print('O maior valor digitado é {}'.format(lista[2]))
