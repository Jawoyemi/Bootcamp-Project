import random

class Hero:
  ITEMS = ["Axe", "Gun", "Rocket Launcher", "Shovel"]

  def __init__(self, username):
    self.username = username
    self.item = random.choice(self.ITEMS)
    self.attack = random.randint(10, 20)
    self.defense = random.randint(15, 25)
    self.health = random.randint(300, 500)
    self.agility = random.randint(30, 60)

  def profile(self):
    return {
      "username": self.username,
      "item": self.item,
      "attack": self.attack,
      "defense": self.defense,
      "health": self.health,
      "agility": self.agility
    }