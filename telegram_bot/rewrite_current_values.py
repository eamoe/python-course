def get_current_values(file_location):
    file = open(file_location, 'r')
    buffer = file.readline()
    file.close()
    values_list = buffer.split(';')
    player = values_list[0].split('=')[1]
    remaining_candies = values_list[1].split('=')[1]
    max_take = values_list[2].split('=')[1]
    return [player, remaining_candies, max_take]


def set_current_values(file_location, who_moves, remaining_candies, max_take):
    file = open(file_location, 'w')
    current_values_str = f"player={who_moves};remaining_candies={remaining_candies};max_take={max_take}"
    file.write(current_values_str)
    file.close()
