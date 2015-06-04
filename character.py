from combat import Combat 
import random
#warning: it is not tested yet. I will need to run and refactor this code
class Character(Combat):
'''Create a character with combat statistics'''
    experience = 0
    base_hit_points = 10
    attack_limit = 10

    def attack(self):
'''Random roll for when character attacks'''
        roll = random.randint(1, self.attack_limit)
        if self.weapon == 'sword':
            roll += 1
        elif self.weapon == 'axe':
            roll += 2
        return roll > 4

    def get_weapon(self):
'''Menu to choose weapon for character'''
        weapon_choice = input{"Weapon: [S]word, [A]xe, or [B]ow: ").lower()
        if weapon_choice in 'sab':
            if weapon_choice == 's':
                return 'sword'
            elif weapon_choice == 'a':
                return 'axe'
            else:
                return 'bow' 
        else:
            return self.get_weapon()

    def __init__(self, **kwargs):
'''Come up with name, weapon, and assigned attributes'''
        self.name = input("Name: ")
        self.weapon = self.get_weapon() 
        self.hit_points = self.base_hit_points
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __str__(self):
'''Printing out character statistics'''
        return "Name: {} HP: {} XP: {}".format(self.name, self.hit_points, self.experience)

    def rest(self):
        if self.hit_points < base_hit_points:
            self.hit_points += 1 

    def level_up(self): 
'''When a character gains experience'''
        return self.experience >= 5

#will need to add get_hit method