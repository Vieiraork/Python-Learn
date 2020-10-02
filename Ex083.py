p1 = p2 = soma = 0

expressao = str(input('Digite a expressão matemática: '))

for p in expressao:
    if p == '(':
        p1 += 1
    if p == ')':
        p2 += 1
soma = p1 + p2

if soma % 2 == 0 and p1 != 0 and p2 != 0:
    print('Expressão válida!')
else:
    print('Expressão inválida, tente novamente!')
