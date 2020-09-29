informatica = ('Ryzen 5 3600', 1500, 'Asus Prime B450M-Gaming/BR', 713,
               'Memória 8GB DDR4 2666MHz', 348,
               'RX 5600XT', 2338, 'Fonte THERMALTAKE SMART RGB 700W', 657)
soma = 0
total = 0

print('-' * 50)
print(f'{"Lista de preços":^50}')
print('-' * 50)

for item in range(0, len(informatica)):
    total += 1
    if item % 2 == 0:
        print(f'{informatica[item]:.<40}', end='')
    if item % 2 == 1:
        print(f'R$ {informatica[item]:.>4.2f}')
        soma += informatica[item]

print('-' * 50)
print(f'{"Total":^50}')
print('-' * 50)
print(f'{total:.<34} ', end='')
print(f'R$ {soma:>4.2f}')
