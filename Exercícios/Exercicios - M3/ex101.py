#print('Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.')

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano_nascimento
    if 18 <= idade < 70:
        print(f'Com {idade} anos, o voto é: OBRIGATÓRIO!')
    elif 16 <= idade < 18 or idade >= 70:
        print(f'Com {idade} anos, o voto é: FACULTATIVO!')
    else:
        print(f'Com {idade} anos, NÃO VOTA!')


ano_nascimento = int(input('Ano de Nascimento: '))
voto(ano_nascimento)
