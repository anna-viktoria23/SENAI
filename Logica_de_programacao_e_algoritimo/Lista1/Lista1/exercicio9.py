#-*- coding: UTF-8 -*-

print("Me de as informações (altura e peso) que eu irei calcular seu IMC, e te indicarei se você está com o peso favoravel ou não.")

altura= float(input("Digite sua altura: "))
peso= float(input("digite seu peso: "))

conta= peso/(altura**2)

if conta<=19.9 and conta>=0:
    print("Você esta abaixo do peso")
elif conta>20 and conta<=24.9:
    print("Seu peso está normal")
elif conta>=25 and conta<=29.9:
    print("você está sobre peso")
elif conta>=30 and conta<=40:
    print("Você está obeso")
elif conta>40:
    print("Você está com obesidade mórbida")
