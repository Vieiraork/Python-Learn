from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
sexo = str(input('Digite seu sexo, M para masculino ou F para feminino: ')).lower().strip()
atual = date.today().year - ano

if sexo == 'm':
    if atual < 18:
        print('O ano do seu alistamento é {} e faltam {} anos para chegar.'.format(ano + 18, (18 - atual)))
    elif atual == 18:
        print('Prepare-se para uma nova jornada, pois você já tem {} anos e pode se alistar'.format(atual))
    elif atual > 18:
        print('Já se passaram {} anos desde o seu alistamento'.format(atual - 18))
        print('E o ano do seu alistamento foi {}.'.format(ano + 18))
else:
    print('O serviço militar não é obrigatório para mulheres.')
