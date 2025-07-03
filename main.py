from villian import Villian
from hero import Hero
from clan import Clan, clan_battle
import getpass

def create_hero():
  username = input("Enter your username: ")
  while True:
    password = getpass.getpass("Enter your password: ")
    confirm_password = getpass.getpass("Confirm your password: ")
    if password == confirm_password:
      break
    print("passwords do not match. Please try again.")
  hero = Hero(username)
  print(f"Hero created successfully! Welcome, {hero.username}!")
  return hero

def battle(hero, villian):
  print(f"\nBattle Start! {hero.username} vs {villian.name}")
  while hero.health > 0 and villian.health > 0:
    # Hero's turn to attack
    damage = max(0, hero.attack - villian.defense)
    villian.health -= damage
    print(f"You attacked the {villian.name} for {damage} damage. Enemy health is now {villian.health}.")
    if villian.health <= 0:
      print(f"You defeated the {villian.name}!")
      return
    # Villian's turn to attack
    damage = max(0, villian.attack - hero.defense)
    hero.health -= damage
    print(f"The {villian.name} attacked you for {damage} damage. Your health is now {hero.health}.")
    if hero.health <= 0:
      print("You have been defeated!")
      return

def join_clan(hero):
  clan_name = input("Enter the name of the clan you want to join: ")
  clan = Clan(clan_name, hero)
  print(f"You have joined the clan: {clan.name}!")
  return clan

def main():
  hero = create_hero()
  path = input("Choose your path(Arena/Forest): ").strip().lower()
  if path == "arena":
    villian = Villian()
    battle(hero, villian)
  elif path == "forest":
    join = input("Do you want to join a clan? (yes/no): ").strip().lower()
    if join == "yes":
      clan = join_clan(hero)
      villian = Villian()
      clan_battle(clan, villian)
    else:
        print("You chose to fight alone in the forest.")
  else:
    print("Invalid path. Please choose either Arena or Forest.")

if __name__ == "__main__":
  main()
    