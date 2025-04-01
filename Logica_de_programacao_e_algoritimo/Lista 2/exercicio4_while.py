# -*- coding: UTF-8 -*-

print("Olá usuário! me de varios numeros e no final eu irei te mostrar a soma dos numeros pares e dos numeros impares. este programa acaba quando um valor maior que 1000 for digitado")

pares= 0
impares= 0

while True:
    n= int(input("Digite seus valores: "))
    if n > 1000:
        print("Você escolheu sair,tchauu! ;)")
        break
    if n % 2 == 0:
        pares = pares + n
    elif n % 2 != 0:
        impares = impares + n
print("A soma dos numeros impares foi de: ", impares, "E a soma dos numeros pares foi de: ", pares)
