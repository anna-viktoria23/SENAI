#Questão 5

#-*- coding: UTF-8 -*-

print("""Olá usuário! Neste programa eu irei te ajudar a calcular o bônus do salário.
caso ele seja menor que 1500,00, seu bônus será de 15%.
E caso ele seja maior, seu bônus será de 10%""")

n1= float(input("Digite o valor do sue saário: "))

if n1 < 1500.00:
    porc= (n1 * 15)/ 100
    print(f"O seu bônus foi de 15%. foi de: {porc:.2f}")
elif n1 > 1500.00:
    porc= (n1 * 10)/ 100
    print(f"O seu bônus foi de 10%. foi de: {porc:.2f}")
else:
    print("Algo deu errado. Por favor, reinicie o programa")
