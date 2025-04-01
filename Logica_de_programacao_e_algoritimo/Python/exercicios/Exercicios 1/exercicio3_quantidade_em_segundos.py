
#-*- coding: UTF-8 -*-
print("olá usuário, irei  te informar o total de segundos com base na sua quantidade de dias, horas, minutos e segundos")
dia= int(input("digite sua quantidade de dias: "))
horas= int(input("Digite sua hora: "))
minutos= int(input("digite os minutos: "))
segundos= int(input("digite seus segundos: "))


dia_pseg= dia * 24 * 60 * 60 * 60
horas_pseg= horas * 60 * 60
minutos_pseg= minutos * 60

soma= dia_pseg + horas_pseg + minutos_pseg + segundos

print("O resultado em segundos é de: ",soma)
