primeiro = int(input('Digite o primeiro termo da prograssão aritmética: '))
razao = int(input('Digite a razão: '))
soma = primeiro

for i in range(primeiro, primeiro+10):
    soma += razao
    print('Os termos da PA são {}'.format(soma))
