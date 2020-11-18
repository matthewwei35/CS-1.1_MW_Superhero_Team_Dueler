# -----------------
# hero.py
# -----------------
import random

# Hero Class
class Hero:
    def __init__(self, name, starting_health = 100):
        '''
        Instance properties:
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
    
    def fight(self, opponent):
        '''
        Current Hero will take turns fighting the opponent hero passed in.
        '''
        hero_list = []
        hero_list.extend([self.name, opponent.name])
        print(f"{random.choice(hero_list)} won!")
    
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)
