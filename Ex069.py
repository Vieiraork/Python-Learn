homens = mulheres = pessoas = 0

while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        pessoas += 1
    if sexo in 'F' and idade < 20:
        mulheres += 1
    if sexo in 'M':
        homens += 1

    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    print('-=-' * 20)

    if continuar in 'N':
        break

print('{} pessoa(s) maior(es) de idade'.format(pessoas))
print('{} mulher(es) menor(es) de 20 anos'.format(mulheres))
print('{} homem(ns) cadatrado(s)'.format(homens))
