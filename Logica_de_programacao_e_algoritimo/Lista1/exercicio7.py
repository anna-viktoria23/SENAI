#-*- coding: UTF-8 -*-

print("Me de um numero de horas trabalhadas, a cada horas empresa vai pagar R$19.50, e recolhe-se para o importo de rendo um valor de 10%,a penas se for acima de R$1.500")

n1= int(input("Me de o total de hora trabalhadas: "))
salario= n1*19.50
imposto= salario*0.10
resposta_final= salario-imposto

if n1>1.500:
        print("O valor á receber é de: ",resposta_final)
else:
    print("O salario a receber é de: ",salario)
