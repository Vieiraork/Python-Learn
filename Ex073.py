brasileirao = ('Atlético-MG', 'Internacional', 'São Paulo', 'Palmeiras', 'Vasco da Gama', 'Flamengo', 'Fluminense',
               'Sport Recife', 'Santos', 'Fortaleza', 'Athletico-PR', 'Ceará SC', 'Atlético-GO', 'Grêmio',
               'Corinthians', 'Coritiba', 'Bragantino-SP', 'Botafogo', 'Goiás', 'Bahia')
linha = '-=-' * 20
alfabetica = sorted(brasileirao)

print('Os cinco primeiros times')
for times in range(0, 5):
    print(f'{times+1}º lugar {brasileirao[times]}')

print(linha)
print('Os quatro últimos times')
for ultimos in range(16, 20):
    print(f'{ultimos+1}º {brasileirao[ultimos]}')

print(linha)
print('Times em ordem alfabética')
for ordem, alfa in enumerate(alfabetica):
    print(f'{ordem+1:2}º {alfa}')

print(linha)
print('Em que posição está o time do Flamengo')
for pos, fla in enumerate(brasileirao):
    if fla == 'Flamengo':
        print(f'O {fla} está na {pos}º colocado no campeonato brasileiro.')
'''
    ou print('o Flamengo está em {brasileirao.index('Flamengo')}')
'''
