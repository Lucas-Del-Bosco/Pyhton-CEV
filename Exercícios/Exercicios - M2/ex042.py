print('Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:\n– EQUILÁTERO: todos os lados iguais\n– ISÓSCELES: dois lados iguais, um diferente\n– ESCALENO: todos os lados diferentes')

l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('O triângulo é possível.')
    if l1 == l2 == l3:
        print('O triângulo é \33[31mEQUILÁTERO\33[m!')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('O trinângulo é \33[31mISÓSCELES\33[m!')
    elif l1 != l2 != l3:
        print('O triângulo é \33[31mESCALENO\33[m!')
else:
    print('O triângulo não é possível.')





