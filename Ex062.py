numero = int(input('Digite um número: '))
razao = int(input('Digite a razão da PA: '))
cont = 1
mais = 10
total = 0

while mais != 0:
    total += mais
    while cont < total:
        print('{} -> '.format(numero), end='')
        numero += razao
        cont += 1
    print('Pausa...')
    mais = int(input('Quantos números deseja mostrar? '))
print('Finalizando a rotina e foram mostrados {} termo(s).'.format(total))

# Refazer esse exercício
