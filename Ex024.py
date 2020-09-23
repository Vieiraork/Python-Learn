cidade = input('Digite o nome de uma cidade: ').strip()

print(cidade[:5].upper() == 'SANTO')

if cidade.upper().split()[0] == 'SANTO':
    print('O nome da cidade começa com SANTO!')
elif cidade.upper().split()[0] != 'SANTO':
    print('O nome da cidade não começa com SANTO!')
