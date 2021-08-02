"""
Custom game exceptions
"""

from datetime import datetime


class GameOver(Exception):
    """
    saving the final score of players at the end of the game
    """

    @staticmethod
    def scores(player_obj):
        """
        Writing and reading the results of players
        :param player_obj: player object
        :return: Name and score of player
        """
        with open('scores.txt', 'a') as scores:
            scores.write(f'{player_obj.score} {player_obj.name} '
                         f'{str(datetime.now().replace(microsecond=0))}\n')
            print(f'\nSee you soon, {player_obj.name}!\n'
                  f'Your score: {player_obj.score}\n')


class EnemyDown(Exception):
    """
    Exception when enemy down
    """


class InvalidLiteral(Exception):
    """
    Input validation error
    """
