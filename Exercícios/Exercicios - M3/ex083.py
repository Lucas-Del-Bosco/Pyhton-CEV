#print('Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.')

'''expressão = str(input('Digite a expressão: '))
pilha = []
for símb in expressão:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão é inválida!')''' #GUANABARA

paren = []
cont = 0
exp = str(input('Digite a sua expressão: '))
for c in exp:
    if c == '(':
        cont += 1
    if c == ')':
        cont -= 1
    if cont < 0:
        break
if cont == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')


