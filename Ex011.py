larg = float(input("Digite a largura da sua parede: "))
altu = float(input("digite a altura da sua parede: "))
area = larg * altu
print("Sua parede tem as dimensões {}x{} e sua área é de {}m2".format(larg, altu, area))
tinta = area / 2
print("Para pintar essa parede, você precisará de {}l de tinta".format(tinta))