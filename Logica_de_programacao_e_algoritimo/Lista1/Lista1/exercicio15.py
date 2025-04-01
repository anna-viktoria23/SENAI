
#-*- coding: UTF-8 -*-

print("Me de a Temperatura atual, que  eu irei lhe dizer como está o clima")
t = float(input("Digite a temperatura: "))
if t <= 15:
    print("Muito Frio")
elif t >= 16 and t <= 23:
    print("Frio")
elif t >= 24 and t <= 26:
    print("Ameno")
elif t >= 26 and t <= 30:
    print("Quente")
elif t >= 31:
    print("Muito Quente")

