#print('Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).')

cont = soma = num = 0
print('Digite um número inteiro, sendo 999 para encerrar o programa!')
while num != 999:
    num = int(input('Número: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'''
Soma: {soma}
Qt. Números: {cont}''')
