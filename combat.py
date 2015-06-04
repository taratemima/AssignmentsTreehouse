import random
#warning: it is not tested yet. I will need to run and refactor this code
class Combat:
'''Class for dodge and attack statistics and acts'''
    dodge_limit = 6
    attack_limit = 6

    def dodge(self):
'''Determine success of dodge'''
        roll = random.randint(1, self.dodge_limit)
        return roll > 4 

    def attack(self):
'''Determine success of attack'''
        roll = random.randint(1, self.attack_limit)
        return roll > 4

