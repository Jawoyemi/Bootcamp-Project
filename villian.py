import random

class Villian:
  def __init__(self, name= "Wolf"):
      self.name = name
      self.attack = random.randint(30, 50)
      self.defense = random.randint(10, 20)
      self.health = random.randint(2000, 3000)
      self.agility = random.randint(10, 30)

  def profile(self):
      return {
        "name": self.name,
        "attack": self.attack,
        "defense": self.defense,
        "health": self.health,
        "agility": self.agility
      }