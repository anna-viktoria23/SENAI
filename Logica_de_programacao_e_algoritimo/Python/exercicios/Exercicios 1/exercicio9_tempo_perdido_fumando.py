print("vamos calcular a quantidade de tempo perdido de vida, fumando cigarros")

cigarros: int(input("Digite a quantidade de cigarros fumados em um dia: "))

anos_fumando= float(input("Digite a quantidade de anos fumados: "))

qnt_total_cigarros= cigarros * anos_fumando * 365

tempo_minutos= qnt_total_cigarros * 10

total_dias= tempo_minutos / 60/ 24

ptint("seu total de tempo perdido foi de: ", Total_dias)
