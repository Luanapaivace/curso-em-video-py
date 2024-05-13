n = int(input("Digite um número inteiro: "))
print("-_-" * 10)
print("""Qual será a base de conversão?
[1] converter para binário
[2] converter para octal
[3] converter para hexagonal""")
print("-_-" * 10)
op = int(input("Deseja converter para 1, 2 ou 3: "))
if op == 1:
    print("Seu número escolhido {} convertido para binário fica igual a {}".format(n, bin(n)))
elif op == 2:
    print("Seu número escolhido {} convertido para octal fica igual a {}".format(n, oct(n)))
elif op == 3: 
    print("Seu número escolhido {} converido para hexagonal fica igual a {}".format(n, hex(n)))


