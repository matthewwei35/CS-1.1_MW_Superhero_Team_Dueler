# -----------------
# hero.py
# -----------------
import random
from ability import Ability
from armor import Armor

# Hero Class
class Hero:
    def __init__(self, name, starting_health = 100):
        '''
        Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
    
    def fight(self, opponent):
        '''
        Current Hero will take turns fighting the opponent hero passed in.
        '''
        # hero_list = []
        # hero_list.extend([self.name, opponent.name])
        # print(f"{random.choice(hero_list)} won!")
        if len(self.abilities) <= 0 and len(opponent.abilities) <= 0:
            print("Draw!")
        else:
            while self.is_alive() and opponent.is_alive():
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
            if self.is_alive() == False:
                print(f"{opponent.name} won!")
            else:
                print(f"{self.name} won!")
                    
    def add_ability(self, ability):
        '''
        Add ability to abilities list.
        '''
        self.abilities.append(ability)

    def attack(self):
        '''
        Calculate the total damage from all ability attacks.
        return
        ------
        total_damage: Int
        '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        '''
        Add armor to self.armors.
        parameters
        ----------
        armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self, damage_amt):
        '''
        Calculate the total block amount from all armor blocks.
        return
        ------
        total_block: Int
        '''
        total_block = 0
        if len(self.armors) > 0:
            for armor in self.armors:
                total_block += armor.block()
            damage_amt -= total_block
            return total_block
        else:
            return total_block

    def take_damage(self, damage):
        '''
        Updates self.current_health to reflect the damage minus the defense.
        '''
        total_damage = damage - self.defend(damage)
        self.current_health -= total_damage

    def is_alive(self):
        '''
        Return True or False depending on whether the hero is alive or not.
        '''
        if self.current_health <= 0:
            return False
        else:
            return True
    
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
    