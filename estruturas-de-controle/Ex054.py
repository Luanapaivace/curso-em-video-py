pesos = [float(input('Peso da {}º pessoa: '.format(a))) for a in range(1, 6)]
print('O maior peso foi de {}Kg\n'
      'O menor foi de {}Kg!'.format(max(pesos), min(pesos)))