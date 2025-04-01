# -*- coding: UTF-8 -*-

print("Oi usuario. me de a quantidade de numeros desejados que eu lhe informarei quantos numeros entre 100 e 200 foram digitados, ou pararei o programa  quando o valor lido for 0.")

vl = 0

while True:
    val = float(input("Digite seu valor: "))
    if val == 0:
        print("Você escolheu sair. tchauu :(")
        break
    if val >= 100 and val <=200:
        vl = vl + 1
print ("Os valores digitados entre 100 e 200 foi de: ", vl)
