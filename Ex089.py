lista = []
notas = []
estudante = []
media = cont = 0

while True:
    nome = str(input('Digite seu nome: '))
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))

    media = (n1 + n2) / 2

    lista.append(nome)

    notas.append(n1)
    notas.append(n2)
    notas.append(media)

    lista.append(notas[:])
    estudante.append(lista[:])

    lista.clear()
    notas.clear()

    op = input('Deseja continuar? [S/N]: ').strip().upper()
    print('-*-' * 10)

    if op in 'N':
        break

print(f'{"Nº":2}       {"Nome":^9}       {"Média":^3}')
for i in estudante:
    print('{:1}        {:^9}        {:^3}'.format(cont, i[0], i[1][2]))
    cont += 1

while True:
    aluno = int(input('Digite o número do aluno para ver suas notas: [999 fechar]: '))

    if aluno == 999:
        break
    if len(estudante) - 1 >= aluno:
        print(f'{estudante[aluno][1][:2]}')
    else:
        print('O aluno com o número digitado não existe, tente novamente.')
