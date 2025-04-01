
#-*- coding: UTF-8 -*-

print("Me diga qual preço da mercadoria e a porcentagem de desconto dela que eu lhe direi qual o desconto e o preço a pagar")
num1= float(input("Preço da mercadoria: "))
num2= float(input("porcentagem do desconto: "))

desconto= num1 * num2 /100

produto_final= num2 - desconto

print("O valor do desconto é de: ", desconto, "E o preço do valor com o desconto é de ",produto_final)
