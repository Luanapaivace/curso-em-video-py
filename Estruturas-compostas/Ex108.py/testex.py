import moedax

p = float(input("Digite o preço em reais: "))
print(f"A metade de {moedax.moedax(p)} é {moedax.meta(p, True)}")
print(f"O dobro de {moedax.moedax(p)} é {moedax.dobrar(p, True)}")
print(f"Aumentando 10%, temos {moedax.aumentar(p, True)}")
print(f"Diminuido 10%, temos {moedax.diminuir(p, True)}")