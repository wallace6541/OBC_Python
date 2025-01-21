"""
Contagem Regressiva
Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”.

Tabuada
Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário
"""

# Lançamento do foguete
import winsound
x = 10
while x >= 0:
    print(x)
    x -= 1
winsound.Beep(1000, 100)

# Tabuada
number = int(input("Tabuada de: \n"))
begin = int(input("De: \n"))
end = int(input("Até: \n"))

x = begin

while x <= end:
    print(f"Tabuada de {number} x {x} = {number * x}")
    x = x + 1