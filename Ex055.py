peso = [0]*5

for i in range(5):
    peso[i] = int(input('Digite o {}º peso: '.format(i+1)))

print('O maior peso digitado é {}'.format(min(peso)))
print('O menor peso digitado é {}'.format(max(peso)))
