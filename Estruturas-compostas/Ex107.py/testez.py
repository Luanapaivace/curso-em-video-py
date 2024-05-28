import moedaz

p = float(input("Digite o preço em reais: "))
print(f"A metade de {moedaz.moedaz(p)} é {moedaz.moedaz(moedaz.meta(p))}")
print(f"O dobro de {moedaz.moedaz(p)} é {moedaz.moedaz(moedaz.dobrar(p))}")
print(f"Aumentando 10%, temos {moedaz.moedaz(moedaz.aumentar(p))}")
print(f"Diminuido 10%, temos {moedaz.moedaz(moedaz.diminuir(p))}")