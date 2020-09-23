casa = float(input('Digite o valor da casa que deseja comprar R$'))
salario = float(input('Digite o seu salário atual R$'))
anos = int(input('Digite em quantos anos deseja efetuar o pagamento '))

prestacao = casa / (anos * 12)
porcentagem = salario * 0.30

if prestacao <= porcentagem:
    print('Parabéns meu caro cliente, seu crédito foi aprovado!')
    print('O valor da casa é R${}, será pago em {} anos e sua prestação sairá R${:.2f}'.format(casa, anos, prestacao))
elif prestacao > porcentagem:
    print('Infelizmente o valor da parcela excedeu os 30% do seu salário, por isso temos que negar o imprestimo.')
