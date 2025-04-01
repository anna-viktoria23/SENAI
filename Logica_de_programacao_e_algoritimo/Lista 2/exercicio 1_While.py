# -*- coding: UTF-8 -*-

print ("Olá usuário! me de os valores desejados e eu irei calcular a soma e a média desses valores")

n1= float(input("Digite o numero desejado: "))
con= 0
val= 0

while n1 >= -1:
    print (n1)
    con= con + 1
    media= con
    val= val + con
    n1= float(input("Digite o valor positivo, ou um negativo para sair: "))
    if n1 == 0:
        media = con + 1
        break
r= val/media
print ("a media dos numeros inseridos foi de: ", r)
