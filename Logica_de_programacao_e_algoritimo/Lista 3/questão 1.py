# -*- coding: UTF-8 -*-
 
print("Olá usuário! Neste programa, eu irei calcular o volume de um cilindro com base nos valores que você me der do raio e da altura :)")
r = 0
a = 0
r = float(input("Digite o valor do raio: "))
a = float(input("Digite o valor da altura: "))
resultado_r = r * r
pi = 3.14

def volume (resultado_r, a, pi):
    return ( resultado_r * a * pi)

total = (volume(resultado_r, a, pi))
print (f"O valor total é: {total:.2f}")
