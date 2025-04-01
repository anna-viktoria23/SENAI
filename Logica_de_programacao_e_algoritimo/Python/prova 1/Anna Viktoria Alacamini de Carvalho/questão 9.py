#Questão 9

#-*- coding: UTF-8 -*-

print("Olá usuário! Neste programa eu irei te dizer se um triângulo é ou não equilátero")

n1= float(input("Digite o valor do primeiro lado: "))
n2= float(input("Digite o valor do segundo lado: "))
n3= float(input("Digite o valor do terceiro lado: "))


if n1==n2==n3 or n2==n3==n1 or n3==n1==n2:
    print("o triangulo é equilátero")
elif n1!=n2==n3 or n2!=n3==n2 or n3!=n1==n2:
    print("O triangulo não é equilátero")
elif n1!=n2!=n3 or n2!=n3!=n1 or n3!=n1!=n2:
    print("O triangulo não é equilátero")
else:
    print("Algo deu errado, por favor reinicie")
