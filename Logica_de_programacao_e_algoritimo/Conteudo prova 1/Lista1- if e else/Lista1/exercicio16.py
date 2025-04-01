
#-*- coding: UTF-8 -*-

print('Me de sua idade, que vou classificar sua faixa etária')
ida = int(input("Digite sua idade: "))  

if ida <= 2:
    print("Bebe")
elif ida > 2 and ida <= 12:
    print("Crianca")
elif ida > 12 and ida <= 23:
    print("Adolescente")
elif ida > 23 and ida <= 70:
    print("Adulto")
else:
    print("Idoso")
