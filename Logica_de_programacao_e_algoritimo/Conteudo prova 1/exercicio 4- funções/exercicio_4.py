# -*- coding: UTF-8 -*-

print("Ola usuario, me da a base e altura de um triangulo, que eu vou lhe retounar sua area")
b = float(input("Digite a base"))
a = float(input("Digite a altura"))

def area(b, a):
    a = (b * a) / 2
    return a
print("A area do triangulo é de",area(a, b))
