import moeda

p = float(input("Digite o preço em reais: "))
print(f"A metade de {p} é {moeda.meta(p)}")
print(f"O dobro de {p} é {moeda.dobrar(p)}")
print(f"Aumentando 10%, temos {moeda.aumentar(p)}")
print(f"Diminuido 10%, temos {moeda.diminuir(p)}")