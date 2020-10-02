valores = []
maior = manor = 0
indice = [0]*2

for num in range(5):
    valores.append(int(input(f'Digite o {num+1}º valor: ')))

for i in range(5):
    if i == 0:
        maior = valores[i]
        menor = valores[i]

    if valores[i] > maior:
        maior = valores[i]
        indice[0] = i

    if valores[i] < menor:
        menor = valores[i]
        indice[1] = i

print(f'{"Resolução":-^55}')
print(f'O maior valor digitado foi {maior} e se encontra na {indice[0] + 1}ª posição.')
print(f'O menor valor digitado foi {menor} e se encontra na {indice[1] + 1}ª posição')

