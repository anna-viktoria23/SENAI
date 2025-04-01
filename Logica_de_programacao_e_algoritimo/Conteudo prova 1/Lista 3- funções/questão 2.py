# -*- coding: UTF-8 -*-

print("Olá usuário! Neste programa se o numero for de 123, o resultado deverá ser 1*2*3=6. Caso o número seja negativo ou zero, a funçâo deve retornar com uma mensagem :)")
n1=int(input("Digite seu valor: "))
a= 1

def cal_de_prod(n1):
    global a
    for i in range(n1-1,0,-1):
        if n1 % i == 0:
            a = a * i
    if n1 == a:
        print("número bom ;)")
    else:
        print("número nao muito legal :(")
cal_de_prod(n1)
