#-*- coding: UTF-8 -*-

print("Digite sua velocidade e eu lhe direi se você esta certo ou se foi multado, caso for, tambem direi o valor da multa")

vel= int(input("Digite a velocidade do carro: "))
if vel < 81:
    print("Você está livre")
else:
    print("Você foi multado, e o valor é de: ", (vel - 80) * 5)




        
