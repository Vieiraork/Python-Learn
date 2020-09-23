lista = []
for i in range(3):
    num = int(input('Digite o {}º número: '.format(i+1)))
    lista.append(num)
    
print('O maior valor digitado é {}'.format(max(lista)))
print('O menor valor digitado é {}'.format(min(lista)))
