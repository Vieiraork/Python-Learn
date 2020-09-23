from datetime import date

ano = int(input('Digite um ano ou se preferir digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} digitado é bisexto!'.format(ano))
else:
    print('O ano {} digitado não é bisexto!'.format(ano))
