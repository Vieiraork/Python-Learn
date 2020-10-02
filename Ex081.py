lista = []

while True:
    lista.append(int(input('Digite um numero: ')))
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    print(f'{"":-^40}')

    if opcao in 'N':
        break

lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números.')
print(f'A lista dos valores em ordem decrescente {lista}')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
