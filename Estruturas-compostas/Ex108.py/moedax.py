def aumentar(preco = 0, formato = False):
    res = preco + (preco * 10/100)
    return res if formato is False else moedax(res)

def diminuir(preco = 0, formato = False):
    res = preco - (preco * 10/100)
    return res if formato is False else moedax(res)

def dobrar(preco = 0, formato = False):
    res = preco * 2
    return res if not formato else moedax(res)

def meta(preco = 0, formato = False):
    res = preco / 2
    return res if not formato else moedax(res)


def moedax(preco = 0, moedax = "R$"):
    return f"{moedax}{preco:.2f}".replace(".", ",")