# -*- coding: UTF-8 -*-

import math

print("Ola usuairo, me da um raio, e vou lhe dizer para retornar a area do circulo")
r = float(input("Digite o raio"))
def area(r):
    pi = math . pi
    area = pi * r ** 2
    return area
print("O circulo a area dele é de", area(r))
