from datetime import date
maior = 0
menor = 0
atual = date.today().year

for i in range(7):
    nascimento = int(input('Digite o ano do seu nascimento: '))
    idade = atual - nascimento

    if idade > 20:
        maior += 1
    elif idade > 0 and idade < 21:
        menor += 1

print('A quantidade de pessoas que são maiores de idade é {}'.format(maior))
print('A quantidade de pessoas que são menores de idade é {}'.format(menor))
