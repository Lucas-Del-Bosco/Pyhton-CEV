#print('Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)')

def leiaInt(txt):
    while True:
        número = str(input(txt))
        if número.isnumeric() is False:
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
        else:
            return número


#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}!')
