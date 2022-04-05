#print('Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:\nA) Quantas vezes apareceu o valor 9.\nB) Em que posição foi digitado o primeiro valor 3.\nC) Quais foram os números pares.')

num = int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite um terceiro número: ')), int(input('Digite o último número: '))
print(f'Você digitou os números: {num}')
print(f'O valor 9 apareceu {num.count(9)} vez(es)!')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição!')
else:
    print('O número 3 não foi digitado!')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
