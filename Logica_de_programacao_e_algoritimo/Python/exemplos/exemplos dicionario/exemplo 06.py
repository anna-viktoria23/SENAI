#Exemplo 22: Exclusão de uma associação do dicionário.

# -*- coding: UTF-8 -*-

tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}

print(tabela)

del tabela["Tomate"]

print(tabela)
