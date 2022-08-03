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
def fill_stats(games):

    game_stats_per_team = list()

    for game in games:
        
        is_finished = 1

        first_team_name = game[0]
        first_team_goals = game[1]
        first_team_victory = 0
        first_team_defeat = 0
        first_team_draw = 0
        first_team_score = 0
        
        second_team_name = game[2]
        second_team_goals = game[3]
        second_team_victory = 0
        second_team_defeat = 0
        second_team_draw = 0
        second_team_score = 0

        if int(first_team_goals) > int(second_team_goals):
            first_team_victory = 1
            first_team_score = 3
            second_team_defeat = 1
        elif int(first_team_goals) < int(second_team_goals):
            second_team_victory = 1
            second_team_score = 3
            first_team_defeat = 1
        elif int(first_team_goals) == int(second_team_goals):
            first_team_draw = 1
            second_team_draw = 1
            first_team_score = 1
            second_team_score = 1 

        game_stats_per_team.append([first_team_name,
                                    is_finished,
                                    first_team_victory,
                                    first_team_draw,
                                    first_team_defeat,
                                    first_team_score])

        game_stats_per_team.append([second_team_name,
                                    is_finished,
                                    second_team_victory,
                                    second_team_draw,
                                    second_team_defeat,
                                    second_team_score])
    
    return game_stats_per_team

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
game_scores = fill_stats(all_games)
results_table = create_stats_dictionary(game_scores)
print_stats_dictionary(results_table)