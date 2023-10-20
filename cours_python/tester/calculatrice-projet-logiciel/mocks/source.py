import time


def request():
    time.sleep(10)
    return 10


def main_function():
    response = request()
    return response


class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_info(self):
        infos = {"name": self.name,
                 "level": self.level}
        return infos


def create_player():
    player = Player("Ranga", 100)
    infos = player.get_info()
    return infos


PI = 3, 1415


def perimeter(radius):
    return 2 * PI * radius


class Weapon:
    def __init__(self, damage_point):
        self.damage_point = damage_point

    def damage(self):
        return self.damage_point


class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon
        self.life_point = 100

    def attack(self, fighter):
        fighter.life_point -= self.weapon.damage()

    def get_life_point(self):
        return self.life_point
