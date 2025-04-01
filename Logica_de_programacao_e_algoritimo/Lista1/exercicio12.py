#-*- coding: UTF-8 -*-

print("Me de dois valores inteiros que eu os colocarei em ordem crescente")

n1= int(input("Digite o primeiro valor: "))
n2= int(input("Digite o segundo valor: "))

if n1 > n2:
    A= n2
    B=n1
    print("O Numero" ,A, "é a menor")
    print("O numero" ,B, "é o maior")
elif n2 > n1:
    A= n1
    B= n2
    print("O Numero" ,A, "é a menor")
    print("O numero" ,B, "é o maior")
