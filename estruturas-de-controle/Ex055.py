lista_nome = []
lista_nome_homem = []
lista_idade = []
lista_sexo = []
lista_idade_homem = []
lista_idade_mulher = []

for c in range (1,5):
    print('-------------- {}ª pessoa ----------------'.format(c))
    nome = str(input('Digite o nome: ')).strip().upper()
    lista_nome.append(nome)

    idade = int(input('Digite a idade: '))
    lista_idade.append(idade)

    sexo = str(input('Digie o sexo M/F: ')).strip().upper()
    lista_sexo.append(sexo)

    if sexo == 'M':
        lista_nome_homem.append(nome)
        lista_idade_homem.append(idade)
    if sexo == 'F' and idade < 20:
        lista_idade_mulher.append(idade)

print('A média de idade do grupo é {}'.format(sum(lista_idade)/len(lista_idade)))
print('Nome do homem mais velho: {}'.format(lista_nome_homem[lista_idade_homem.index(max(lista_idade_homem))]))
print('O total de mulheres abaixo de 20 anos: {}'.format(len(lista_idade_mulher)))


