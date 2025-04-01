13# -*- coding: UTF-8 -*-


print("Ola usuario, me da dois numeros que eu vou lhe dizer para retornar somente o meio dele")
um = float(input("Digite um numero"))
dois = float(input("Digite outro numero"))
def contar(um, dois):
    if um == dois:
        print("Deu erro, os 2 numero são iguais")
    elif um < dois:
            print("O segundo numero é maior", dois)
    else:
            print("O primeiro numero é maior", um)
contar( um, dois)
