from time import sleep
soma = tg = qp = qn = menor = 0
while True:
    nome = str(input("Digite o nome do produto: ")).strip().upper()
    valor = float(input("Digite o valor do produto: "))
    de = " "
    soma += valor
    qn += 1
    while de not in "SN":
        de = str(input("Deseja continuar? ")).strip().upper()[0]
    if valor > 1000:
        qp += 1
    if qn == 1:
       menor = valor 
    if de == "S":
        print("OK, VAMOS PARA O PRÓXIMO PRODUTO")
    elif de == "N":
        print("OK, FINALIZANDO PESQUISA...")
        break
sleep(2)
print("FIM DA PESQUISA")
sleep(1)
print("-=-" * 18)
print("DETALHES DA PESQUISA:")
print(" ")
print(f"A SOMA DOS VALORES DE TODOS OS PRODUTOS É {soma} REAIS")
print(f"TEVE {qp} PRODUTOS QUE PASSARAM DE 1000 REAIS")
print(f"O NOME DO PRODUTO COM MENOR VALOR FOI O/A {nome}")
print("-=-" * 18)
