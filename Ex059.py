from time import sleep
opcao = 0
soma = 0
mult = 0


def menu():
    print('''Digite uma das opções
        1 - Somar números
        2 - Multiplicar números
        3 - Maior número
        4 - Novos números
        5 - Sair do programa
    ''')


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

while opcao != 5:
    menu()
    print('-=-' * 20)
    opcao = int(input('Digite uma das opções: '))
    print('-=-' * 20)

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre {} x {} = {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            print('O primeiro número é o maior e seu valor é {}.'.format(n1))
        elif n1 < n2:
            print('O segundo número é o maior e seu valor é {}.'.format(n2))
        else:
            print('Os dois números são iguais!')
    elif opcao == 4:
        n1 = int(input('Digite um novo valor para o primeiro número: '))
        n2 = int(input('Digite um novo valor para o segundo número: '))
    elif opcao == 5:
        print('Finalizando programa...')
        sleep(1)
    else:
        print('Opção inválida, por favor tente novamente.')

print('Rotina finalizada!')
