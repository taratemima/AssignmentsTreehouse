import random
#warning: it is not tested yet. I will need to run and refactor this code
class Combat:
    dodge_limit = 6
    attack_limit = 6

    def dodge(self):
        roll = random.randint(1, self.dodge_limit)
        return roll > 4 

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        return roll > 4

