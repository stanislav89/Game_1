"""
Contains player, enemy and scores classes
"""
from random import randint

from exceptions import GameOver, EnemyDown, InvalidLiteral
from settings import DEFAULT_LIVES_COUNT, ALLOWED_MOVES


class Enemy:
    """
    The Enemy class
    """

    lives = 1
    level = 1

    def __init__(self, name, level):
        """
        Construction the name and level of the enemy
        :param name: enemy name
        :param level: enemy level
        """
        self.name = name
        self.lives = level

    @staticmethod
    def select_attack():
        """
        Method for generate random int number
        :return: number from 1 to 3
        """
        return randint(1, 3)

    def decrease_lives(self, player_obj):
        """
        Method for decrease lives from enemy and add to player
        :param player_obj: player object
        :return: exception EnemyDown
        """
        self.lives -= 1
        if self.lives <= 0:
            self.level += 1
            raise EnemyDown
        player_obj.score += 1


class Player:
    """
    The Player class
    """
    allowed_attack = 0
    score = 0
    lives = DEFAULT_LIVES_COUNT
    level = 1

    def __init__(self, name):
        """
        Construction the name player
        :param name: player name
        """
        self.name = name

    @staticmethod
    def fight(attack, defense):
        """
        :return result of round
        """
        if attack == defense:
            return 0
        if ((defense - attack) == 1) or ((attack - defense) == 2):
            return 1
        if ((defense - attack) == -1) or ((attack - defense) == -2):
            return -1

    def decrease_lives(self):
        """
        Method for decrease lives from player
        :return: exception Game over
        """
        self.lives -= 1
        if self.lives <= 0:
            GameOver.scores(self)
            raise GameOver

    def attack(self, enemy_obj):
        """
        Method for determining the result of a player's attack
        :param enemy_obj: Enemy object
        :return: message with result of attack
        """
        if self.allowed_attack in ALLOWED_MOVES:
            result = self.fight(int(self.allowed_attack), enemy_obj.select_attack())

            if result == 0:
                print("It's a draw!")
            elif result == 1:
                print("You attacked successfully!")
                enemy_obj.decrease_lives(self)
            else:
                print("You missed!")
        else:
            raise InvalidLiteral

    def defence(self, enemy_obj):
        """
        Method for determining the result of a player's defence
        :param enemy_obj: Enemy object
        :return: message with result of defence
        """
        if self.allowed_attack in ALLOWED_MOVES:
            result = Player.fight(enemy_obj.select_attack(), int(self.allowed_attack))
            if result == 0:
                print("It's a draw!")

            elif result == 1:
                print("Enemy attacked successfully!")
                self.decrease_lives()
            else:
                print("Enemy missed!")
        else:
            raise InvalidLiteral


class Scores:
    """
    Top 10 players only
    """

    @staticmethod
    def show_score():
        """
        Method for generate and print scores table
        :return: scores table
        """

        with open('scores.txt', 'r') as scores:
            sort_scores = sorted(scores.readlines(), reverse=True, key=lambda score: int(score[:2]))
            scores = [i.split() for i in sort_scores]
            scores_table = range(1, 11 if len(scores) > 10 else len(scores) + 1)
            for i in zip(scores_table, scores):
                print(f'{i[0]}. {i[1][1]} : {i[1][0]} | {i[1][-2]} {i[1][-1]}')
