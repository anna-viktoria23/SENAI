#Questão10

#-*- coding: UTF-8 -*-

print("""Olá usuário! neste programa eu te ajudarei a saber o valor da taxa de serviço da
sua conta de restaurante :)""")

n1= float(input("Digite o valor da sua conta: "))

if n1 > 200:
    porc= (n1 * 8)/ 100
    print(f"O valor da taxa de serviço ficou de: {porc}")
elif n1 <= 200:
    porc= (n1 * 10)/100
    print(f"O valor da taxa de serviço será de: {porc}")
else:
    print("Algo deu errado, por favor reinicie")

