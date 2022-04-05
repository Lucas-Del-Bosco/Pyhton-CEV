#print('Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.')

def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar um valor!')
            return 0
        else:
            return n


def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (TypeError, ValueError):
            print('\033[31mERRO: Digite um valor inteiro válido!')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar um valor real válido!')
            return 0
        else:
            return n


num = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um número Real: ')
print(f'Você digitou os número {num} e {num2}')
