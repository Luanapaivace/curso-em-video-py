distancia = float(input("Qual a distância da sua viagem? "))
print("Você está prestes a começar uma viagem de {}km".format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print("E o preço da sua passagem será de {}".format(preco))