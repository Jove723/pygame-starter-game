import pygame
import time
import random

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} has been defeated!")

    def is_alive(self):
        return self.hp > 0
    
    

class Hero(Character):
    def __init__(self, name, hp, attack, defense, x, y):
        super().__init__(name, hp, attack)
        self.defense = defense
        self.x = x
        self.y = y
        self.speed = 5
        self.last_attack_time = 0
        self.attack_cooldown = 2

    def take_damage(self, amount):
        # Reduce damage based on defense
        damage = max(0, amount - self.defense)
        super().take_damage(damage)

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed

    def can_attack(self):
        return time.time() - self.last_attack_time > self.attack_cooldown
    
    def attack_enemy(self, enemy):
        if self.can_attack():
            print(f"{self.name} attacks {enemy.name}")
            enemy.take_damage(self.attack)
            self.last_attack_time = time.time()

class Enemy(Character):
    def __init__(self, name, hp, attack):
        super().__init__(name, hp, attack)
        self.last_attack_time = 0
        self.attack_cooldown = random.uniform(1.5, 3.0)

    def can_attack(self):
        return time.time() - self.last_attack_time > self.attack_cooldown
    
    def attack_hero(self, hero):
        if self.can_attack():
            print(f"{self.name} attacks {hero.name}")
            hero.take_damage(self.attack)
            self.last_attack_time = time.time()
            self.attack_cooldown = random.uniform(1.5, 3.0)



