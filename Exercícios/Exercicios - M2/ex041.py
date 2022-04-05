print('A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:\n– Até 9 anos: MIRIM\n– Até 14 anos: INFANTIL\n– Até 19 anos: JÚNIOR\n– Até 25 anos: SÊNIOR\n– Acima de 25 anos: MASTER')

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade <= 9:
    print(f'Você tem {idade} anos.')
    print('Você faz parte da categoria \33[31mMIRIM\33[m!')
elif 9 < idade <= 14:
    print(f'Você tem {idade} anos.')
    print('Você faz parte da categoria \33[32mINFATIL\33[m!')
elif 14 < idade <= 19:
    print(f'Você tem {idade} anos.')
    print('Você faz parte da categoria \33[33mJÚNIOR\33[m!')
elif 19 < idade <= 25:
    print(f'Você tem {idade} anos.')
    print('Você faz parte da categoria \33[34mSÊNIOR\33[m!')
else:
    print(f'Você tem {idade} anos.')
    print('Você faz parte da categoria \33[35mMASTER\33[m!')

