dias = int(input('Digite a quantidade de dias passados com o carro: '))
km = float(input('Digite a quantidade de km percorrido: '))

pagamento = (dias * 60) + (km * 0.15)

print('A distância percorrida foi de {:.2f}km na quantidade de dias {} e isso custa R${:.2f}.'
      .format(km, dias, pagamento))
