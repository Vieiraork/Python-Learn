soma = p1 = p2 = 0

expressao = str(input('Digite a expressão matemática: '))

for p in expressao:
    if p == '(' or p == ')':
        soma += 1

if soma % 2 == 0 and soma != 0:
    print('Expressão válida!')
else:
    print('Expressão inválida, tente novamente!')
