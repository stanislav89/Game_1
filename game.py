"""
Main file with the launch of the gameplay
"""

import names

import settings
from exceptions import GameOver, EnemyDown, InvalidLiteral
from models import Player, Enemy, Scores


def play():
    """
    Input player name, input commands for game settings and create player object and enemy object.
    :return: Result of game
    """
    level = 1
    player_name = input('Please enter your name: ')
    print(f"  Welcome to the game, {player_name}!\n"
          f"__________________________________________\n")
    player = Player(player_name)
    enemy_name = names.get_first_name(gender='male')
    enemy = Enemy(enemy_name, level)

    while True:
        command = input(f"{player_name}, please enter \"START\" to start the game\n"
                        "    or enter \"HELP\" to show any commands: ").lower()

        if command == "start":
            print(f'Your enemy name is {enemy_name}!')
            while True:
                try:
                    player.allowed_attack = input('Please make a choice for attack: '
                                                  '\'1\' - Wizard, \'2\' - Warrior,'
                                                  ' \'3\' - Bandit ')
                    player.attack(enemy)
                    print(f'Your lives: {player.lives} | {enemy_name} lives: {enemy.lives}\n')
                    player.allowed_attack = input('Please make a choice for defence: '
                                                  '\'1\' - Wizard, \'2\' - Warrior,'
                                                  ' \'3\' - Bandit ')
                    player.defence(enemy)
                    print(f'Your lives: {player.lives} | {enemy_name} lives: {enemy.lives}\n')
                except EnemyDown:
                    player.score += 5
                    player.level += 1
                    level += 1
                    print(f'\n********************************************\n'
                          f' You killed {enemy_name}. Your score: '
                          f'{player.score}. Level: {player.level}.\n'
                          f'********************************************\n')
                    enemy_name = names.get_first_name(gender='male')
                    enemy = Enemy(enemy_name, level)
                    print(f'\nYour enemy name is {enemy_name}!\n')
                except InvalidLiteral:
                    print('\nThere are no other characters in this game!\n')

        if command == "show scores":
            print('\n')
            Scores.show_score()
            print('\n')

        if command == "help":
            print(f'\nAllowed commands: {", ".join(settings.ALLOWED_COMMANDS)}.\n')

        if command == "exit":
            raise KeyboardInterrupt


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        print('GAME OVER')
    except KeyboardInterrupt:
        pass
    finally:
        print('Goodbye!')
