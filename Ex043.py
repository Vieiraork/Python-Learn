peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está abaixo do peso e seu imc é {:.1f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal e seu imc é {:.1f}'.format(imc))
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso e seu imc é {:.1f}'.format(imc))
elif imc >= 30 and imc < 40:
    print('Você está com obesidade e seu imc é {:.1f}'.format(imc))
elif imc >= 40:
    print('Você precisa se cuidar, pois está com obesidade móbida e seu imc é {:.2f}'.format(imc))
