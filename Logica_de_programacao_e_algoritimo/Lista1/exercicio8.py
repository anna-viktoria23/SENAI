#-*- coding: UTF-8 -*-

print("Me de o valor do seu salario bruto e o da prestação que eu lhe informarei se você podera ou não receber o emprestimo")

n1= float(input("Digite o valor do seu salário: "))
n2= float(input("Digite o valor da prestação: "))

porc_sal= (n1*30)/100

if n2>porc_sal:
    print("O emprestimo não poderá ser concebido")
else:
    print ("o emprestimo pode ser concebido")
