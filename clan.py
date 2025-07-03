#battling with the clan against the villian
from hero import Hero


class Clan:
  def __init__(self, name, leader):
    self.name = name
    self.members = [leader]
    #Adds two random AI clanmates
    for i in range(2):
      member = Hero(f"ClanMate{i+1}")
      self.members.append(member)

  def total_attack(self):
    return sum(member.attack for member in self.members)
  
  def total_defense(self):
    return sum(member.defense for member in self.members)
  
  def total_health(self):
    return sum(member.health for member in self.members)

def clan_battle(clan, villian):
  print(f"\nClan Battle Start! {clan.name} vs {villian.name}")
  clan_health = clan.total_health()
  while clan_health > 9 and villian.health > 0:
    # clan attacks villian
    damage = max(0, clan.total_attack() - villian.defense)
    villian.health -= damage
    print(f"The clan attacked the {villian.name} for {damage} damage. Villian health is now {villian.health}.")
    if villian.health <= 0:
      print(f"The clan defeated the {villian.name}!")
      return
    # villian attacks clan
    damage = max(0, villian.attack - clan.total_defense())  
    clan_health -= damage
    print(f"The {villian.name} attacked the clan for {damage} damage. Clan health is now {clan_health}.")
    if clan_health <= 0:
      print("The clan has been defeated!")
      return