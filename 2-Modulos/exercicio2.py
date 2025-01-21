"""
Crie duas funções em python para agendar o desligamento do computador em uma hora e meia hora.
"""

import os

# 1 - Desligar o computador
os.system("shutdown /s") # Desliga a maquina em 60s no windows
# os.system('shutdown /s /t 0') # Desliga a maquina em 0s no windows (imediatamente)
# os.system('shutdown now') # No Linux

# 2 - Cancelar o desligamento
os.system("shutdown /a")

# 3 - Função para desligar o computador em 1 hora
def turn_off_one_hour():
    os.system("shutdown /s /t 3600")
    
# 4 - Função para desligar o computador em 30 min
def turn_off_half_an_hour():
    os.system("shutdown/s /t 1800")
    
def cancel_shutdown():
    os.system("shutdown /a")
    
turn_off_one_hour()
cancel_shutdown()