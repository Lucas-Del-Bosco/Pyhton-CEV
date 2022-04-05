def aumentar(preço, taxa):
    desconto = preço * taxa/100
    total = preço + desconto
    return total


def diminuir(preço, taxa):
    desconto = preço * taxa/100
    total = preço - desconto
    return total


def dobro(preço):
    total = preço * 2
    return total


def metade(preço):
    total = preço / 2
    return total

