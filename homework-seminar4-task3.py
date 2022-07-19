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
    game_result = str(input(f"Игра {game_number}: ")).split(";")
    return game_result


#Get list of all played games
def all_games_list(games_number):
    all_games = list()
    for game in range(games_number):
        all_games.append(get_game_result(game + 1))   
    return all_games

#The function converts list of played games into the scores list:
# [team_name, is_finished, is_victory, is_draw, is_defeat, game_score]
def game_parser(games):

    scores = list()

    for game in games:
        finished_game = 1

        team1_name = game[0]
        team1_goals = game[1]
        team1_victory = 0
        team1_defeat = 0
        team1_draw = 0
        team1_score = 0
        
        team2_name = game[2]
        team2_goals = game[3]
        team2_victory = 0
        team2_defeat = 0
        team2_draw = 0
        team2_score = 0

        if int(team1_goals) > int(team2_goals):
            team1_victory = 1
            team1_score = 3
            team2_defeat = 1
        elif int(team1_goals) < int(team2_goals):
            team2_victory = 1
            team2_score = 3
            team1_defeat = 1
        elif int(team1_goals) == int(team2_goals):
            team1_draw = 1
            team2_draw = 1
            team1_score = 1
            team2_score = 1 

        scores.append([team1_name, finished_game, team1_victory, team1_draw, team1_defeat, team1_score])
        scores.append([team2_name, finished_game, team2_victory, team2_draw, team2_defeat, team2_score])
    
    return scores

def create_stats_dictionary(scores):
    stats_dictionary = {}
    for element in scores:
        team_name = element[0]
        if team_name in stats_dictionary:
            stats_dictionary[team_name][0] = int(stats_dictionary[team_name][0]) + int(element[1])
            stats_dictionary[team_name][1] = int(stats_dictionary[team_name][1]) + int(element[2])
            stats_dictionary[team_name][2] = int(stats_dictionary[team_name][2]) + int(element[3])
            stats_dictionary[team_name][3] = int(stats_dictionary[team_name][3]) + int(element[4])
            stats_dictionary[team_name][4] = int(stats_dictionary[team_name][4]) + int(element[5])
        else:
            stats_dictionary[team_name] = [int(element[1]), int(element[2]), int(element[3]), int(element[4]), int(element[5])]
    
    return stats_dictionary

def print_stats_dictionary(stats):
    for key, value in results_table.items():
        print(f"{key}: {value[0]} {value[1]} {value[2]} {value[3]} {value[4]}")

# Main program
games_number = get_games_number()
all_games = all_games_list(games_number)
game_scores = game_parser(all_games)
results_table = create_stats_dictionary(game_scores)
print_stats_dictionary(results_table)