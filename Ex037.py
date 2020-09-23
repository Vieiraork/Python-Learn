numero = int(input('Digite um número: '))
print('''
Digite o número que corresponde a opção requerida: 
1 - Converter número para binário 
2 - Converter número para octal 
3 - Converter número para hexadecimal 
''')
opcoes = int(input('Digite uma das opções: '))

if opcoes == 1:
    print('O número {} em binário é {}'.format(numero, bin(numero)[2:]))
elif opcoes == 2:
    print('O número {} em octal é {}'.format(numero, oct(numero)[2:]))
elif opcoes == 3:
    print('O número {} em hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Por favor, digite alguma das opções do menu.')
