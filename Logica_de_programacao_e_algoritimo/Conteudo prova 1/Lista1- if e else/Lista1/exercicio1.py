#-*- coding: UTF-8 -*-

print("olá usuario! digite dois numeros e eu lhe trarei o resultado. Caso ele seja maior que 20, somarei mais 8. Se ele for menor ou igual a 20, irei subtrair por 5.")

n1= float(input("Digite seu primeiro valor: "))
n2= float(input("Digite seu segundo valor: "))
soma= n1+n2

if soma>20:
    print("O resultado da sua soma é: " ,soma+8)

else:
    print("o resultado da sua soma é: ",soma-5)
