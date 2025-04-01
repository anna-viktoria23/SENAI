# -*- coding: UTF-8 -*-

print("Olá usuário! Neste programa eu irei lhe dar o resultado de uma opreção matemática do seu desejo :)")

n1= int(input("Digite o primeiro valor: "))
n2= int(input("Digite o segundo valor: "))
op= input("""Coloque a opereção desejada podendo ser: '+' para soma, '/' para divisão
'*' para multiplicação e '-' para subtração: """)

def opereções (op):
    global n1, n2
    if op == "+":
        soma= n1+n2
        print ("O resultado da sua soma é de: ", soma)
    elif op == "-":
        subtração= n1 - n2
        print ("O resultado da sua subtração é de: ", subtração)
    elif op == "*":
        multiplicação= n1 * n2
        print ("O resultadp da multiplicação é de: ", multiplicação)
    elif op == "/":
        divisão= n1/n2
        print ("O resultado da divisão é de: ", divisão)

opereções (op)
