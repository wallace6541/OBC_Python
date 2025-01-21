"""
Escreva um módulo em python para tratar algumas strings e que possua as seguintes funcionalidades:

1.Inverter uma string de trás pra frente.

2.Retornar apenas letras com índice par.

3.Retornar apenas letras com índice ímpar.
"""

import strings

name = input("Digite uma frase\n")

print(strings.inverse(name))

print(strings.even_characters(name))

print(strings.odd_characters(name))