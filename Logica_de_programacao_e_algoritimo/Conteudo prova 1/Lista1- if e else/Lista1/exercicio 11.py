#-*- coding: UTF-8 -*-

print ("Me de sua nota final ue eu lhe direi se você esta de reprovado, recuperação ou aprovado")

nota= float(input("Digite sua nota: "))

if nota>=0 and nota<=2.9:
    print("Você foi reprovado")
elif nota>=3 and nota<=6.9:
    print("Você ficou de recuperação")
else:
    print("Você foi aprovado")
