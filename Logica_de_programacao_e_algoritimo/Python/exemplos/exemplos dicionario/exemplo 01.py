#Exemplo 17: Funcionamento do dicionário.

# -*- coding: UTF-8 -*-

tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}

print(tabela["Tomate"])

print(tabela)

tabela["Tomate"] = 2.50

print(tabela["Tomate"])

tabela["Cebola"] = 1.20

print(tabela)
