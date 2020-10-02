valores = []
for vl in range(3):
    valores.append(int(input(f'Digite o {vl+1}º número: ')))

for num in valores:
    print(f'{num} -> ', end='')
print('Acabou')

'''
    Criar uma cópia da lista
    a = [1, 2, 3]
    b = a[:]
    
    
    Ligação entre as listas
    a = [1, 2, 3]
    b = a
'''
