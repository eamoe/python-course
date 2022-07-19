# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча
# и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.

# Sample Input:
#3
#Спартак;9;Зенит;10
#Локомотив;12;Зенит;3
#Спартак;8;Локомотив;15

#Sample Output:
#Спартак:2 0 0 2 0
#Зенит:2 1 0 1 3
#Локомотив:2 2 0 0 6

#Get number of played games
def get_games_number():
    
    games_number = int(input("Введите количество сыгранных игр: "))

    return games_number

#Get results of a single game
def get_game_result(game_number):
    
    game_result = list()
    print(f"Игра {game_number}:")
    game_result = str(input("")).split(";")
    
    return game_result

#Get list of all played games
def all_games_list(games_number):
    all_games = list()
    for game in range(games_number):
        all_games.append(get_game_result(game + 1))
    
    return all_games


# Main program
games_number = get_games_number()

all_games = all_games_list(games_number)

game_scores = list()
for game in all_games:
    team1_name = game[0]
    team1_goals = game[1]
    team2_name = game[2]
    team2_goals = game[3]

    finished_game = 1

    team1_victory = 0
    team1_defeat = 0
    team1_draw = 0
    team1_score = 0
    
    team2_victory = 0
    team2_defeat = 0
    team2_draw = 0
    team2_score = 0

    if int(team1_goals) > int(team2_goals):
        team1_victory = 1
        team2_defeat = 1
        team1_score = 3
    if int(team1_goals) < int(team2_goals):
        team2_victory = 1
        team1_defeat = 1
        team2_score = 3
    if int(team1_goals) == int(team2_goals):
        team1_draw = 1
        team2_draw = 1
        team1_score = 1
        team2_score = 1 

    game_scores.append([team1_name, finished_game, team1_victory, team1_draw, team1_defeat, team1_score])
    game_scores.append([team2_name, finished_game, team2_victory, team2_draw, team2_defeat, team2_score])

results_table = {}
for element in game_scores:
    team_name = element[0]
    if team_name in results_table:
        results_table[team_name][0] = int(results_table[team_name][0]) + element[1]
        results_table[team_name][1] = int(results_table[team_name][1]) + element[2]
        results_table[team_name][2] = int(results_table[team_name][2]) + element[3]
        results_table[team_name][3] = int(results_table[team_name][3]) + element[4]
        results_table[team_name][4] = int(results_table[team_name][4]) + element[5]
    else:
        results_table[team_name] = [element[1], element[2], element[3], element[4], element[5]]

for key, value in results_table.items():
    print(f"{key}: {value[0]} {value[1]} {value[2]} {value[3]} {value[4]}")