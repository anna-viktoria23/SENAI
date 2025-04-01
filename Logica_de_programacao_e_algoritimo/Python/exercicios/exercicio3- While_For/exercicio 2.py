# -*- coding: UTF-8 -*-

print("Olá usuario! me de a quantidade de valores que eu irei te falar quantos numeros foram digitados. caso você digite um numero negativo, o programa ira parar")

v = 0
while True:
    val  = int(input("Digite o valor desejado ou um numero negativo para sair: "))
    if val <=0:
        print("Você escolheu sair :(")
        v = v + 1
        print ("O total de valores digitados foram de: ",v)
        break
    if val > 0:
        v = v + 1
    print ("O total de valores digitados foram de: ",v)
