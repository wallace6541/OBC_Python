"""
Cálculo da Distância
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, 
cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,35 para viagens mais longas.

Aumento salário funcionário
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
"""

 #Calculo da Distancia
distance = float(input("digite a distancia a percorrer\n"))
if distance <= 200:
    ticket = 0.5 * distance
else:
    ticket = 0.35 * distance
print(f"preço da passagem é {ticket:.2f}")


#Aumento do salário

salario = float(input("Digite seu salario"))
perc_increase = 0.15
if salario > 1250:
    perc_increase = 0.10
increase = salario * perc_increase
print(f"Seu aumento sera de {increase:.2f}\n")