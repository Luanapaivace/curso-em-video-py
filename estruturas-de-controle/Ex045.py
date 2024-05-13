from time import sleep
print ("-=-" * 15)
print("Contagem regressiva para a explosão dos fogos: ")
print("-=-" * 15)
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print("BOOOM!!!")