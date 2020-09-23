cores = {'Branco': '\033[1:30m', 'Vermelho': '\033[1:31m', 'Default': '\033[0m'}

salario = int(input('Digite seu salário: '))

if salario > 0:
    if salario > 1250:
        aumento = (salario * 0.10) + salario
    else:
        aumento = (salario * 0.15) + salario
else:
    print('Digite valores numéricos acima de 0 para o salário!')

print('Quem ganhava {}R${}{} agora ganha {}R${}'
      .format(cores['Vermelho'], salario, cores['Default'], cores['Branco'], aumento))
