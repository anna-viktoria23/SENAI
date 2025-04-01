#-*- coding: UTF-8 -*-

print("me de dois numeros, que eu irei te pedir a operação e eu irei resolve-lá para você")

num1= int(input("Digite seu primeiro valor: "))
num2= int(input("Digite seu segundo valor: "))
operacao= input("de a operação desejada: ")

if operacao== "+":
          print(num1+num2)
elif operacao == "-":
    print(num1 - num2)
elif operacao == "*":
    print(num1 * num2)
elif operacao == "/":
    print (num1 / num2)


