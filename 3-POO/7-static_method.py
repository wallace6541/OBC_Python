"""
1 - O método estático não utiliza o parâmetro referente a classe.
2 - O método estático pode acessar mas não pode modificar o estado da classe.
3 - Usamos o decorator @Classmethod para criar um método de classe
"""

class Course:
    def __init__(self, name, trail):
        self.name = name
        self.trail = trail
        
    @staticmethod
    def courses_trail(trail):
        if trail == "Python Fundamentos":
            courses = ["Dominando o Python", "Módulos Pip", "Orientação a Objetos"]
        elif trail == "Automação com o Python":
            courses = ["Automação de Tarefas", "Web Scraping", "Assistente Virtual em Python"]
        else:
            courses = ["A definir"]
        return courses
            
print(Course.courses_trail("Python Fundamentos"))
print(Course.courses_trail("Análise de Dados"))
print(Course.courses_trail("Automação com o Python"))