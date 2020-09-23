sexo = str(input('Digite o seu sexo (M/F): ')).strip()[0]

while sexo not in 'MmFf':
    sexo = str(input('Digite somente (M/F): ')).strip()[0]
print('Obrigado por informar corretamente seu sexo!')
