somaid = 0
maioridade = 0
nomevelho = ''
menorvinte = 0

for p in range(1, 5):
    print('---------- {}ª pessoa ----------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).upper().strip()

    somaid += idade

    if idade > maioridade and sexo == 'M':
        maioridade = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        menorvinte += 1

print('A média de idade do grupo é {} anos.'.format(somaid/4))
print('O homem mais velho se chama {} e sua idade {} anos.'.format(nomevelho, maioridade))
print('São {} mulher(es) menor(es) de 20 anos.'.format(menorvinte))
