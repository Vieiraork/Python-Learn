from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - ano

if idade < 10:
    print('O atleta tem {} anos e pertence a categoria MIRIM'.format(idade))
elif idade > 9 and idade < 15:
    print('O atleta tem {} anos e pertence a categoria INFANTIL'.format(idade))
elif idade > 14 and idade < 20:
    print('O atleta tem {} anos e pertence a categoria JUNIOR'.format(idade))
elif idade < 26:
    print('O atleta tem {} anos e pertence a categoria SÊNIOR'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos e pertence a categoria MASTER'.format(idade))
