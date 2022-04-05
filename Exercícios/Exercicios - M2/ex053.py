print('Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:')

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'Você digitou a frase {inverso}')
if junto == inverso:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')
