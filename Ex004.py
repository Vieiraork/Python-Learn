algo = input('Digite algo: ')

print('É númerico? {}'.format(algo.isnumeric()))
print('É alfa númerico? {}'.format(algo.isalnum()))
print('É maiusculo? {}'.format(algo.isupper()))
print('É alfabético? {}'.format(algo.isalpha()))
print('Tem somente espaços? {}'.format(algo.isspace()))
print('Está em minusculo? {}'.format(algo.islower()))