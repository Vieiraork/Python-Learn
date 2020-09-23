l = [0] * 3

for i in range(3):
    l[i] = float(input('Digite o {}º lado: '.format(i+1)))

if l[0] < l[1] + l[2] and l[1] < l[2] + l[0] and l[2] < l[1] + l[0]:
    if l[0] == l[1] and l[0] == l[2]:
        print('Todos as medidas são iguais, por isso o triângulo formado é o Equilátero.')
    elif l[0] == l[1] or l[1] == l[2] or l[2] == l[0]:
        print('Duas das medidas são iguais, por isso o triângulo formado é o Isósceles.')
    elif l[0] != l[1] and l[0] != l[2]:
        print('Todas as medidas são diferentes, por isso o triângulo formado é o Escaleno.')
else:
    print('As medidas fornecidas não foram um triângulo.')
