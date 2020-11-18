# -----------------
# armor.py
# -----------------
import random

# Armor Class
class Armor:
    def __init__(self, name, max_block):
        '''
        Instance properties:
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        '''
        Return a random value between 0 and the initialized max_block strength.
        '''
        random_value = random.randint(0, self.max_block)
        return random_value

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())
