def get_action():
    with open("telegram_bot_organization/action.csv", 'r') as file:
        action = file.read()
    return action

def set_action(action):
    with open("telegram_bot_organization/action.csv", 'w') as file:
        file.write(action)