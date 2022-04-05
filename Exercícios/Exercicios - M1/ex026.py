print('Faça um programa que leia uma frase pelo teclado e mostre quantas: '
'Vezes aparece a letra “A”\nEm que posição ela aparece a primeira vez\nEm que posição ela aparece a última vez.')

frase = str(input('Digite uma frase: ')).strip().lower()
#frasea = frase.count('a')
print(f'A letra A aparece {frase.count("a")} vezes')
print(f'A primeira letra A apareceu na posição {frase.find("a")+1}')
print(f'A última letra A apareceu na posição {frase.rfind("a")+1}')








