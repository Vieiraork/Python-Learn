l1 = float(input('Digite o valor para o primeiro lado: '))
l2 = float(input('Digite o valor para o segundo lado: '))
l3 = float(input('Digite o valor para o terceiro lado: '))

l12 = l1 - l2
l23 = l2 - l3
l31 = l3 - l1

if l12 < l3 and l12 < l1 + l3:
    if l23 < l1 and l23 < l2 + l1:
        if l31 < l2 and l31 < l3 + l2:
            print('Essas medidas são válidas para um triângulo!')
        else:
            print('Infelizmente a terceira medida não permite a formação do triângulo!')
    else:
        print('Infelizmente a segunda medida não permite a formação do triângulo!')
else:
    print('Infelizmente a primeira medida não permite a formação do triângulo!')
