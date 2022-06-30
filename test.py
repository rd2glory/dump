import random

class BattleBot:
  def __init__(self,name):
    self.name = name
    self.health = 100.0
    self.base_armor = 10.0
    self.base_damage = 10.0
    self.speed = 10.0

  def attack(self,opponent):
    damage_dealt = self.base_damage - (self.base_damage*opponent.base_armor/100)
    opponent.take_damage(damage_dealt)

  def take_damage(self,damage_dealt):
    self.health -= damage_dealt

  def get_stats(self):
    print("Name:",self.name)
    print("Attack:",str(self.base_damage))
    print("Armor:",str(self.base_armor))
    print("Speed:",str(self.speed))
    print("Health:",str(self.health))
    print()

  def action(self,opponent):
    random_number = random.randint(0,100)
    if random_number <= 20:
      self.build_armor()
    elif random_number <= 40:
      self.build_attack()
    elif random_number <= 60:
      self.build_speed()
    elif random_number <= 90:
      self.attack(opponent)
    else:
      print(self.name,"glitched out!")

  def build_attack(self):
    self.base_damage += 2
    self.speed -= 1
    self.base_armor -= 1

  def build_armor(self):
    self.base_armor += 2
    self.speed -= 1
    self.base_damage -= 1

  def build_speed(self):
    self.speed += 2
    self.base_damage -= 1
    self.base_armor -= 1

  def is_alive(self):
    return self.health>0
