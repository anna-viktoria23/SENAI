#Exemplo 21: Obtenção do preço com dicionário.

# -*- coding: UTF-8 -*-

tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}

while True:
    produto = input("Digite o nome do produto, fim para terminar: ")
    if produto == "fim":
     break
    if produto in tabela:
            print("Preço: %5.2f" % tabela[produto])
    else:
        print("Produto não encontrado!")
