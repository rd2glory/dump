import random

class BattleBot:
    def __init__(self, name):
        self.name = name
        self.health = 100.0
        self.base_armor = 10.0
        self.base_damage = 10.0
        self.speed = 10.0
    def is_alive(self):
        if self.health <= 0:
            return False
        else:
            return True
    def attack(self, opponent):
        damage_dealt = self.base_damage - (self.base_damage * (opponent.base_armor/100))
        opponent.takeDamage(damage_dealt)
    def take_damage(self, damage_dealt):
        self.health -= damage_dealt
    def get_stats(self):
        print(self.name)
        print("Health: " + str(self.health))
        print("Attack: " + str(self.base_damage))
        print("Defense: " + str(self.base_armor))
        print("Speed: " + str(self.speed))
        print()
    def action(self, opponent):
        random_num = random.randint(0, 100)
        if random_num <= 20:
            self.build_armor()
        elif random_num <= 40:
            self.build_attack()
        elif random_num <= 60:
            self.build_speed()
        elif random_num <= 90:
            self.attack(opponent)
        else:
            print(self.name + " glitched out!")
    def build_armor(self):
        self.base_armor += 2
        self.base_damage -= 1
        self.speed -= 1
    def build_attack(self):
        self.base_armor -= 1
        self.base_damage += 2
        self.speed -= 1
    def build_speed(self):
        self.base_armor -= 1
        self.base_damage -= 1
        self.speed += 2
    def is_alive(self):
        return self.health > 0
