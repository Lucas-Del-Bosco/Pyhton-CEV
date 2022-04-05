print('Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:\n– IMC abaixo de 18,5: Abaixo do Peso\n– Entre 18,5 e 25: Peso Ideal\n– 25 até 30: Sobrepeso\n– 30 até 40: Obesidade\n– Acima de 40: Obesidade Mórbida')

altura = float(input('Altura(m): '))
peso = float(input('Peso(Kg): '))
IMC = peso / (altura ** 2)
if IMC < 18.5:
    print(f'Seu IMC é de {IMC:.1f}')
    print('Status: ABAIXO DO PESO.')
elif 18.5 <= IMC < 25:
    print(f'Seu IMC é de {IMC:.1f}')
    print('Status: PESO IDEAL')
elif 25 <= IMC < 30:
    print(f'Seu IMC é de {IMC:.1f}')
    print('Status: SOBREPESO')
elif 30 <= IMC <= 40:
    print(f'Seu IMC é de {IMC:.1f}')
    print('Status: OBESIDADE')
else:
    print(f'Seu IMC é de {IMC:.1f}')
    print('Status: OBESIDADE MÓRBIDA')