velo = int(input("Qual a velocidade atual do carro?" ))
pagar = velo * 7
if velo > 80:
    print("Multado! Você excedeu o limite permitido que é 80km/h")
    print("Você deve pagar uma multa de {}".format(pagar))
else:
    print("Tudo certinho por aqui, tenha um bom dia!")
