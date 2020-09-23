nome = [0]*4
idade = [0]*4
sexo = [0]*4

somador = 0

maior = 0
menor = 0
indicem = 0

for i in range(4):
    nome[i] = str(input('Nome {}ª pessoa: '.format(i+1))).strip()
    idade[i] = int(input('Idade {}ª pessoa: '.format(i+1)))
    sexo[i] = str(input('Sexo {}ª pessoa (M/F): '.format(i+1))).upper()

    somador += idade[i]

    if sexo[i] == 'M' and idade[i] > maior:
        maior = idade[i]
        indicem = i
    if sexo[i] == 'F' and idade[i] < 20:
        menor += 1

print('A média de idade do grupo é {}'.format(somador/4))
print('O homem mais velho do grupo se chama {} e tem {} anos'.format(nome[indicem], idade[indicem]))
print('A quantidade de mulheres menores de 20 anos é {}.'.format(menor))
