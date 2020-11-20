# -----------------
# team.py
# -----------------

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

