n = input('Digite um valor: ')
print(n.isnumeric())
print(n.isalnum())
print('Está em caixa alta? {}'.format(n.isupper()))

"""
    Para retornar o tipo primitivo de um objeto basta utilizar a função type como vemos a seguir
    print(type('nome do objeto'))
    print(n.isnumeric)
    print(n.isalpha)
    print(n.isalnum)
    print(n.isupper)
"""