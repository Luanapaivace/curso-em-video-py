print("-=-" * 6)
print("Caixa eletrônico")
print("-=-" * 6)
valor = int(input("Quantos reais você quer sacar? "))
t = valor
c = 50
tc = 0
while True:
    if t >= c:
        t -= c
        tc += 1
    else:
        if tc > 0:
            print(f"Total de {tc} cédulas de {c} reais")
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 5
        elif c == 5:
            c = 1
        tc = 0
        if t == 0:
            break