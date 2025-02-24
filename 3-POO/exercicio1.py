"""
Desenvolva novas funcionalidades para complementar o nosso gerenciamento da classe Filmes. Segue o escopo das funcionalidades:

1.Uma das funcionalidades requeridas é que o usuário possa realizar a avaliação de um filme passando uma nota com parâmetro e que essa nota seja salva no atributo específico da classe.

2.Assim que uma avaliação for realizada, deve ser incrementado o total de avaliadores daquele filme. Obs: Considere criar um atributo específico para esse fim.

3.Para cada filme ter uma nota de avaliação média que consiste na divisão do total de avaliação pelo total de avaliadores.
"""

class Movie:
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0
        
    def __str__(self):
        return f"Filme: {self.name}"
    
    def techinal_sheet(self):
        print("##--##Dados do Filme##--##")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Está no plano? {self.includedPlan}")
        print(f"Avaliação do filme: {self.totalEvaluation}")
        print(f"Duração do filme: {self.durationMinutes}")
        print(f"Total de Avaliadores: {self.evaluators}\n")
        
    def evaluate(self, note):
        self.totalEvaluation += note #totalEvaluation = totalEvaluation + note
        self.evaluators += 1
        
    def average(self):
        print(f"Média do Filme {self.name}: {self.totalEvaluation / self.evaluators}\n")
        
mario = Movie("Super Mario Bros", 2023, False, 135)
avatar = Movie("Avatar", 2023, False, 180)
mario.evaluate(9.5)
mario.evaluate(10.0)
mario.techinal_sheet()
mario.average()

avatar.evaluate(9.0)
avatar.evaluate(8.0)
avatar.techinal_sheet()
avatar.average()