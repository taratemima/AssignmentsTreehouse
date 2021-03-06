import random
from combat import Combat
'''Second version of monster with more additions'''

COLORS = ['yellow','green','black', 'red', 'blue']
#warning: it is not tested yet. I will need to run and refactor this code

class Monster(Combat):
'''Create new monster with hit points, experience, weapon, and sound'''
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = 'knife'
    sound = 'roar'

    def __init__(self, **kwargs ):
'''Setting up bounds for monster'''
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(COLORS)
        
        for key, value in kwargs.items():
            setattr(self, key, value)
        
    def battlecry(self):
'''What the monster yells'''
        return self.sound.upper()

    def __str__(self):
'''What prints for the monster'''
        return '{} {} HP:{} XP:{} '.format(self.color.title(), self.__class__.__name__, self.hit_points, self.experience)

         #will need to add get_hit method

class Goblin(Monster):
'''statistics for goblins, a type of monster'''
    max_hit_points = 3
    max_hit_points = 2
    sound = 'squeak'

class Troll(Monster):
'''statistics for trolls, a type of monster'''
    min_hit_points = 3
    max_hit_points = 5
    min_experience = 2
    max_experience = 5
    sound = 'growl'

class Dragon(Monster):
'''statistics for dragons, a type of monster'''
    min_hit_points = 5
    max_hit_points = 10
    min_experience = 6
    max_experience = 10
    sound = 'raaaaaaaaaar'
