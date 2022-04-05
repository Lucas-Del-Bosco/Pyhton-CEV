print('Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.')

resposta = 'S'
cont = soma = maior = menor = 0
while resposta == 'S':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    resposta = str(input('Quer continuar? [S/N]: ')).strip()[0].upper()
media = soma / cont
print(f'Você digitou {cont} números, a soma entre eles é {soma}, logo, a média foi de {media}!')
print(f'O maior valor foi {maior} e o menor foi {menor}!')
