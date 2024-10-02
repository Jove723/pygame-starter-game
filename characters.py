import random


class Character:
    def __init__(self, name, hp, attack, image):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.image = image

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)

    def is_alive(self):
        return self.hp > 0

class Player(Character):
    pass

class Enemy(Character):

    def generate_attack(self):
        return random.randint(self.attack - 5, self.attack + 5)
