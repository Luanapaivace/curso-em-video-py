print("-_-" * 15)
print("Emprestimo bancário para a compra de uma casa")
print("-_-" * 15)
valorca = float(input("Qual o valor da casa?"))
salario = float(input("Qual o salário do comprador?"))
pagaranos = int(input("Em quantos anos o comprador irá pagar?"))
p = (salario * 30) / 100
v = (pagaranos * 12) / valorca
if v <= p:
    print("-_-" * 9)
    print("Seu emprestimo foi NEGADO!")
    print("-_-" * 9)
else:
    print("-_-" * 16)
    print("Parabéns sua solitação de emprestimos foi aceita")
    print("-_-" * 16)