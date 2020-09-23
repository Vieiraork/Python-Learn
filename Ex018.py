from math import radians, sin, cos, cos, tan
angulo = int(input('Digite um ângulo qualquer: '))
'''
if angulo == 30:
    print('O seno do ângulo é {:.2f}'.format(1/2))
    print('O cosceno do ângulo é {:.2f}'.format((3 ** 0.5)/2))
    print('A tangente do ângulo é {:.2f}'.format((3 ** 0.5)/3))
elif angulo == 45:
    print('O seno do ângulo é {:.2f}'.format((2 ** 0.5)/2))
    print('O cosceno do ângulo é {:.2f}'.format((2 ** 0.5)/2))
    print('A tangente do ângulo é {:.2f}'.format(1))
elif angulo == 60:
    print('O seno do ângulo é {:.2f}'.format((3 ** 0.5)/2))
    print('O cosceno do ângulo é {:.2f}'.format(1/2))
    print('A tangente do ângulo é {:.2f}'.format(3 ** 0.5))
else:
    print('Digite um ângulo válido.')
'''

seno = sin(radians(angulo))
cosceno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('Para o ângulo de {}° o seno vale {:.2f}'.format(angulo, seno))
print('Para o ângulo de {}° o cosceno vale {:.2f}'.format(angulo, cosceno))
print('Para o ângulo de {}° a tangente vale {:.2f}'.format(angulo, tangente))

