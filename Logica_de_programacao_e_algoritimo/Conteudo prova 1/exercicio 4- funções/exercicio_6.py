
# -*- coding: UTF-8 -*-

print("ola usuario, me de um argumento que retorne (P), caso seu valor for positivo, ou (N), se o caso seja zero ou negativo")
n1 = float(input("me de um valor:"))

def positivo_negativo(n1):
    if n1 > 0:
        print("P")
    else:
        print("N")
positivo_negativo(n1)
