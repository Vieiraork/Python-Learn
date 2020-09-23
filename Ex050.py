# coding: utf-8
soma = 0
for i in range(6):
    num = int(input('Digite o {}º número: '.format(i+1)))
    if num % 2 == 0:
        soma += num
print('A soma dos números pares é {}'.format(soma))
