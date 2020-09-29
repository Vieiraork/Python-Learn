# Tuplas inicio

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche))

print('-=-' * 20)
print('Primeira maneira')
for pedido in lanche:
    print(f'Eu vou comer {pedido}')

print('-=-' * 20)
print('Segunda maneira')
for comida in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[comida]}')

print('-=-' * 20)
print('Teerceira maneira')
for pos, algo in enumerate(lanche):
    print(f'Eu vou comer {algo}, na posicação {pos}')

'''
    Tuplas são estrutuas compostas imutáveis, ou seja, não podemos alterar ou tirar valores apenas acrescentar
'''
