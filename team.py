# -----------------
# team.py
# -----------------
import random
from hero import Hero

# Team Class
class Team():
    def __init__(self, name):
        '''
        Initialize your team with its team name and an empty list of heroes.
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        '''
        Remove the hero from the heroes list. If Hero isn't found return 0.
        '''
        foundHero = False
        # Loop trough each hero in our list
        for hero in self.heroes:
            # If we find them, remove them form the list
            if hero.name == name:
                self.heroes.remove(hero)
                # Set out indicator to True
                foundHero = True
        # If we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not foundHero:
            return 0

    def view_all_heroes(self):
        '''
        Prints out all heroes to the console.
        '''
        for hero in self.heroes:
            print(hero)

    def add_hero(self, hero):
        '''
        Add Hero object to self.heroes.
        '''
        self.heroes.append(hero)

    def stats(self):
        '''
        Print team statistics.
        '''
        for hero in self.heroes:
            try:
                kd = hero.kills / hero.deaths
                print(f"Kill/Deaths: {kd}")
            except ZeroDivisionError:
                print("Divide by zero")

    def revive_heroes(self, health = 100):
        '''
        Reset all heroes health to starting_health.
        '''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        '''
        Battle each team against each other.
        '''
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            random_hero = random.choice(living_heroes)
            random_opponent = random.choice(living_opponents)

            random_hero.fight(random_opponent)

            if random_hero.is_alive() == True and random_opponent.is_alive() == False:
                living_opponents.remove(random_opponent)
            else:
                living_heroes.remove(random_hero)
