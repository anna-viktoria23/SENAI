
#Instrução del é usada para remover elementos da lista.

#Exemplo 13: Remoção de elementos.

# -*- coding: UTF-8 -*-

L = ["a", "b", "c"]

#removeu a posição "2", levando em consideração que começa com 0 (0, 1, 2)----removeu o 1
del L[1]

print (L)

del L[0]

print (L)

#mostra a posição
print (L[0])

#a posição nunca fica vazia
