soma = 0
while True:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero == 999:
        break
    soma += numero
print(f'A soma dos valores é {soma}')

'''
    Loop infinito pode ser parado com o comando break
    Sua estrutura é a seguinte while True:
    Nessa aula também fomos apresentados a interpolação de strings ou f strings
    disponível em outras linguagens ao meu ver facilita o que facilita por exemplo:
        Na interpolação de objetos em query sql
        Lidar melhor com arquivos JSON talvez
    
'''
