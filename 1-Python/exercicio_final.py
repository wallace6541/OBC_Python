"""
Gerenciamento de Jogadores e Times

Escreva um programa em python que realize o gerenciamento de jogadores. Ele deve atender aos seguintes requisitos:

Adicionar um time

Remover um time

Listar times

Adicionar jogador em um time

Remover jogador de um time

Listar jogadores de um time

A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.

A opção de adicionar um time deve pedir um nome para o time que será cadastrado.

A opção de remover um time deve pedir o índice específico do time que foi cadastrado para fazer a sua exclusão.

A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar com o nome do jogador que será adicionado.

A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador que fora cadastrado no time.

A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.

Este é o exercício de revisão do módulo, então aproveite para utilizar todos os recursos vistos até agora, como os funções, condições, loop, listas, etc.
"""

teams = {}
done = False

# Funcao para listar times
def print_teams():
    print("Times Listados:")
    for i, team in enumerate(teams.values()):
        print(f"{i+1}. {team['name']} ({len(team['players'])} jogadores)")
        
# Função para listar jogadores de um time
def print_team_players(team):
    print(f"Jogadores do {team['name']}")
    for i, player in enumerate(team['players']):
        print(f"{i+1}. {player}")


while not done:
    print("O que você deseja fazer?")
    print("1. Adicionar um time")
    print("2. Remover um time")
    print("3. Lista de times")
    print("4. Adicionar jogador em um time")
    print("5. Remover jogador em um time")
    print("6. Listar jogadores de um time")
    print("7. Sair")
    
    choice = input(">")
    if choice == "1":
        team_name = input("Digite o nome do time\n")
        teams[team_name] = {'name': team_name, 'players': []}
        print("Time adicionado.")
    elif choice == "2":
        print_teams()
        team_num = int(input("Informe o número do time que deseja remover \n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            del teams[team_name]
            print("Time removido.")
        else:
            print("Número do time inválido.")
    elif choice == "3":
        print_teams()
    elif choice == "4":
        print_teams()
        team_num = int(input("Informe o número do time que deseja adicionar o jogador \n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            player_name = input("Informe o nome do jogador\n")
            teams[team_name]['players'].append(player_name)
            print("Jogador adicionado no time")
        else:
            print("Número do time está inválido")
            
    elif choice == "5":
        print_teams()
        team_num = int(input("Informe o número do time que deseja remover o jogador\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            print_team_players(teams[team_name])
            player_num = int(input("Informe o número do jogador que deseja remover\n"))
            if player_num <= len(teams[team_name]['players']):
                del teams[team_name]['players'][player_num - 1]
                print("Jogador removido do time")
            else:
                print("Número do jogador inválido")
        else:
            print("Número do time inválido.")
        
    elif choice == "6":
        print_teams()
        team_num = int(input("Informe o número do time que deseja listar os jogadores \n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            print_team_players(teams[team_name])
        else:
            print("Número do time inválido")
            
    elif choice == "7":
        done = True
    else:
        print("Opção inválida")