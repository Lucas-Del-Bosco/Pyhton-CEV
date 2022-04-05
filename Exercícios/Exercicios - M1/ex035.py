print('Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.')

s1 = float(input('Qual a medida do primeiro segmento?: '))
s2 = float(input('Qual a medida do segundo segmento?: '))
s3 = float(input('Qual a medida do terceiro segmento?: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')
