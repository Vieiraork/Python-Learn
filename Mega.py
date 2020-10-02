from random import randint
megasena = []

while len(megasena) < 6:
    resultado = randint(1, 61)

    if resultado not in megasena:
        megasena.append(resultado)

print(f'O resultado da Megasena de hoje é {megasena}')
