
#-*- coding: UTF-8 -*-

print('Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for menor que R$ 20,00; caso contrário, o lucro será de 30%.')
pr = float(input("Digite o valor do produto: "))
if pr < 20:
    l = pr * 45 / 100
    print("O valor do produto com o lucro de 45% é de: ", l)
else:
    lu = pr * 30 / 100
    print("O valor do produto com o lucro de 30% é de: ", lu)

