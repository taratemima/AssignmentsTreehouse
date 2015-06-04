from character import Character
from monster2 import Dragon
from monster2 import Goblin
from monster2  import Troll 

#Missing functions

class Game:
'''Methods for game'''
    def setup(self):
'''Create characters and monsters'''
        self.player = Character()
        self.monsters = [Goblin(), Troll(), Dragon()] 
        self.monster = self.get_next_monster()

    def get_next_monster(self):
'''Get new monster after the one before it is defeated'''
        try:
            return self.monsters.pop(0) 
        except IndexError:
            return None 

    def monsterTurn(self):
'''Monster doing stuff on its turn: attack, wait, or dodge'''
        #Check to see if monster attacks
        #If so, tell the player
        #Check to see if player wants to dodge 
        #If so, see if the dodge is successful 
        #Check to see if monster dodges
        #If dodge is successful, continue
        #If dodge is not successful, remove 1 hit point from player
        #If the monster is not attacking, tell that to the player 

    def playerTurn(self):
'''Player doing stuff on its turn: attack, rest, or quit'''
        #Let the player attack, rest, or quit
        #If player wants to attack, see if attack is successful 
        #If so, see if the monster dodges
        #If monster dodges, print that
        #If monster does not dodge, subtract right number of hit points from monster
        #If attack is not good, tell the player
        #If they rest:
        #call player.rest()
        #If they quit: 
        #exit the game
        #If they type anything else: 
        #rerun this method

    def cleanup(self):
    #if the monster has no more hit points:
    #up the player's experience
    #print a message
    #Get a new monster

    def __init__(self):
        self.setup()
        while self.player_hit_points and (self.monster or self.monsters):
            print(self.player)
            self.monsterTurn()
            self.playerTurn() 
            self.cleanup() 
        if self.player.hit_points:
            print("You win!")
        elif self.monster or self.monsters:
            print("You lose!") 


