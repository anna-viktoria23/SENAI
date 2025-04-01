#Questão4

#-*- coding: UTF-8 -*-

print("""Olá usuário! neste programa eu te informarei se eu valor é:
menor que 10
entre 10 e 20
maior que 20
:)""")

n1= int(input("Digite o seu número: "))

if n1 < 10:
    print("Este número é menor que 10")
elif n1 >= 10 and n1 <= 20:
    print("Este número está entre 10 e 20")
elif n1 > 20:
    print("Este número é maior que 20")
else:
    print("Algo deu errado, por favor reinicie")
