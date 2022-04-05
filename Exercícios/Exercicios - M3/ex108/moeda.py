def aumentar(preço=0, taxa=0):
    desconto = preço * taxa/100
    total = preço + desconto
    return total


def diminuir(preço=0, taxa=0):
    desconto = preço * taxa/100
    total = preço - desconto
    return total


def dobro(preço=0):
    total = preço * 2
    return total


def metade(preço=0):
    total = preço / 2
    return total


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
