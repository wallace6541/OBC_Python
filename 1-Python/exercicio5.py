"""
Conta letras maiúsculas e minúsculas

Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.

Lista números pares e ímpares de uma lista

Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.
"""

# Verificação Letra Maiuscula e Minuscula
def check_char(text):
    type ={"Uppercase": 0, "Lowercase": 0}
    for char in text:
        if char.isupper():
            type["Uppercase"] += 1
        elif char.islower():
            type["Lowercase"] += 1
    print("Texto original:", text)
    print("Número de letras maiúsculas:", type["Uppercase"])
    print("Número de letras minúsculas:", type["Lowercase"])
    
check_char("A Melhor Forma de Prever o Futuro é Criá-lo")

# Verifica número par ou ímpar
def check_numbers(numbers):
    pairs = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            pairs.append(number)
        else:
            odd.append(number)
    return pairs, odd

print(check_numbers([1, 2, 4, 6, 5, 7, 11, 20, 13]))