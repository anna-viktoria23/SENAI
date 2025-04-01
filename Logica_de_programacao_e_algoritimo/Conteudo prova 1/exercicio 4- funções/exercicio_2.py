# -*- coding: UTF-8 -*-

print("Ola usuario, me de dois numeros, que eu vou lhe retornar como True se o primeiro numero for múltiplo do segundo")

um = float(input("Digite um numero"))
dois = float(input("Digite outro numero"))
def multiplo(um, dois):
    if um % dois == 0:
        print("É True")
    else:
        print("É False")
multiplo(um, dois)
