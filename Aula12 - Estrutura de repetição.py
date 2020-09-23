num = int(input('Digite um número: '))

while num <= 0:
    num = int(input('Digite números positivos: '))

for i in range(num):
    print('Posição {:6}'.format(i))
    if i % 2 == 0:
        print('{} é divisível por 2.'.format(i))

'''
    FOR -> sua estrutura no range é a seguinte range(p1, p2, p3)
    p1 -> é o começo do range que a estrutura de repetição irá percorrer
    p2 -> é a posição final para o range
    p3 -> é a iteração, ou seja, a regra que irá submeter o laço de repetição
'''