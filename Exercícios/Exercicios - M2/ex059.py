#print('Crie um programa que leia dois valores e mostre um menu na tela:\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\nSeu programa deverá realizar a operação solicitada em cada caso.')

v1 = int(input('Primeiro Valor: '))
v2 = int(input('Segundo Valor: '))
opção = 0
while opção != 5:
    print('[1] Somar\n[2] Multiplicar\n[3] Maior Valor\n[4] Novos Números\n[5]Sair do Programa')
    opção = int(input('>>>>>>>>> Qual é a opção?: '))
    if opção == 1:
        soma = v1 + v2
        print(f'A soma dos dois valores é {soma}!')
    elif opção == 2:
        multiplicação = v1 * v2
        print(f'A multiplicação entre {v1} e {v2} é {multiplicação}!')
    elif opção == 3:
        if v1 > v2:
            print(f'O maior valor é {v1}!')
        else:
            print(f'O maior valor é {v2}!')
    elif opção == 4:
        v1 = int(input('Primeiro Valor: '))
        v2 = int(input('Segundo Valor: '))
    elif opção == 5:
        print('Fim do Programa. Volte Sempre!')
    else:
        print('Opção inválida')
    print('\33[1;31m==-\33[m' * 15)

