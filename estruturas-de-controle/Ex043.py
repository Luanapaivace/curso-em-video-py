preco = float(input("Qual o valor do produto? "))
print("""Suas opções:
[1] à vista no dinheiro/cheque
[2] à vista no cartão
[3] em até duas vezes no cartão
[4] 3x ou mais no cartão""")
op = int(input("Qual será a forma de pagamento? "))
if op == 1:
    s1 = preco - (preco * 10 / 100)
    print("O valor do produto sendo à vista no dinheiro/cheque ganhará 10% de desconto ficando: {}".format(s1))
elif op == 2:
    s2 = preco - (preco * 5 / 100)
    print("O valor do produto sendo à vista no cartão ganhrá 5% de desconto ficando: {}".format(s2))
elif op == 3:
    print("O valor do produto sendo em até duas vezes no cartão firá com o valor fixo: {}".format(preco))
elif op == 4:
    s3 = preco + (preco * 20 / 100)
    print("O valor do produto  sendo em 3x ou mais no cartão terá 20% de juros ficando: {}".format(s3))