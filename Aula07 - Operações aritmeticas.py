n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

s = n1+n2
su = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
re = n1%n2

print('A soma vale {}, a subtração value {} e a multiplicação vale {}'.format(s, su, m))
print('A divisão vale {:.2f}, a divisão inteira vale {} e o resto vale {}'.format(d, di, re))

"""
    Para divisão inteira usa-se // duas barras
    Para potência usa-se **
    Para modulo ou resto da divisão usa-se %
    
    Ordem de precedencia
    1º vem os parenteses ()
    2º vem a potência **
    3º vem multiplicação, divisâo, divisâo inteira e modulo *, /, //, %
    4 vem soma e subtração +, - ;
"""