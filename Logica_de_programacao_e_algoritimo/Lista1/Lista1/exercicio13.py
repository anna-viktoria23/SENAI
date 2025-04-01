
#-*- coding: UTF-8 -*-

print('Exercicio 13')
print('Ola Usuário, me de três notas, sua média, que eu irei analisar sua situação.')
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
f = int(input("Digite sua quantidade de faltas"))
m = (n1 + n2 + n3) / 3
if m >= 7:
    print("Você foi aprovado")
elif m < 3 or f > 20:
    print("Você foi reprovado")
else:
    print("Você ficou de recuperação")
