n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2)/2

if media < 6:
    print('Você está repovado e sua média é {:.2f}'.format(media))
elif media >= 6:
    print('Você está aprovado e sua média é {:.2f}'.format(media))
