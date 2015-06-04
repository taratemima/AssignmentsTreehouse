import random

COLORS = ['yellow','green','black', 'red', 'blue']

#warning: I have not run and refactor the code, I will do so

class Monster:
'''Creating a monster, including hit points, experience, weapon, and sound'''
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = 'knife'
    sound = 'roar'

#hit_points=5, color='green', weapon='knife', sound='roar'

    def __init__(self, **kwargs ):
        self.hit_points = kwargs.get(hit_points,5)
        self.color = kwargs.get(color,'yellow')
        self.weapon = kwargs.get(weapon,'knife')
        self.sound = kwargs.get(sound,'roar')

    def battlecry(self):
'''What it yells when it is near you'''
        return self.sound.upper()
        

#boss = Monster(hit_points=9000, color='red', weapon='cannon', sound='alala')
#boss.hit_points = 9000
#boss.color = 'red'
#boss.weapon = 'cannon'
#boss.sound = 'alala'
#boss.battlecry()


class Store:
'''Print opening hours for a store'''
    open = 7
    close = 20

    def hours(self):
        return "We are open from {} to {}".format(self.open, self.close)
