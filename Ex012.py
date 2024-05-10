preco = float(input("Qual o preço do produto? "))
des = (preco * 5) / 100
desco = preco - des
print("O produto que custava {}reais, na promoção com o desconto de 5% vai custar{}".format(preco, desco))