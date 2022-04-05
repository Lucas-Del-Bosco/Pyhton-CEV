print('Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.')

n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:\n[1] Converter para BINÁRIO\n[2] Converter para OCTAL\n[3] Converter para HEXADECIMAL')
escolha = int(input('Digite o número desejado: '))
if escolha == 1:
    print(f'O número {n} convertido para BINÁRIO é: {bin(n)[2:]}')
elif escolha == 2:
    print(f'O número {n} convertido para OCTAL é: {oct(n)[2:]}')
elif escolha == 3:
    print(f'O número {n} convertido para HEXADECIMAL é: {hex(n)[2:]} ')
else:
    print('O número informado não é válido')

