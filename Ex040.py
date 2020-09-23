nota = [0] * 2

for i in range(2):
    nota[i] = float(input('Digite a {}º nota: '.format(i+1)))

if nota[0] > 0 and nota[0] <= 10 and nota[1] > 0 and nota[1] <= 10:
    media = (nota[0] + nota[1]) / 2
    if media < 5:
        print('Sua média foi {} e infelizmente você está REPROVADO!'.format(media))
    elif media >= 5 and media < 7:
        print('A sua média foi {} e você está de RECUPERAÇÃO!'.format(media))
    elif media >= 7 and media <= 10:
        print('Parabéns sua média foi {} e você está APROVADO!'.format(media))
else:
    print('Digite valores de 0 até 10.')
