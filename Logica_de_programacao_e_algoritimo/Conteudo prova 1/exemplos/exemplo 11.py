# -*- coding: UTF-8 -*-

cont = 0
acum = 0

while True:
    valor = float(input("""Digite valores e no final lhe darei a média. Digite valor negativo para sair: """))
    if valor <0:
        print("você escolheu sair")
        break
    acum= acum + valor
    cont= cont + valor
print(f"A média dos valores digitados é de:", (acum/cont:.2f))
