numero = [0]*2
for i in range(2):
    numero[i] = int(input('Digite o {}º número: '.format(i+1)))

if numero[0] > numero[1]:
    print('O primeiro valor é maior!')
elif numero[0] < numero[1]:
    print('O segundo valor é maior!')
elif numero[0] == numero[1]:
    print('Os dois valores são iguais!')
