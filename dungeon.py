import random 
'''Written by Tara Edwards for Treehouse'''
'''Uses random.choice for two lists of a range between 0 and 2'''

CELLS = [(0,0), (0,1), (0,2),
        (1,0), (1,1), (1,2),
        (2,0), (2,1), (2,2)]

def get_locations():
  # monster = random
    monsterX = random.choice(range(0,2))
    monsterY = random.choice(range(0,2))
  
  # door = random
    doorX = random.choice(range(0,2))
    doorY = random.choice(range(0,2))

  # start = random
    startX = random.choice(range(0,2))
    startY = random.choice(range(0,2))

  # if monster, door, or start are the same, do it again
    startX, startY = reroll(startX, startY, monsterX, monsterY)
    startX, startY = reroll(startX, startY, doorX, doorY)
    doorX, doorY = reroll(monsterX, monsterY, doorX, doorY)
#No sense getting eaten just before you escape 
    monster_coord = (monsterX, monsterY)
    door_coord = (doorX, doorY)
    start_coord = (startX, startY)
    
    return monster_coord, door_coord, start_coord 
  
  # return monster, door, start
  
def reroll(playerX, playerY, otherX, otherY):
    if playerX == otherX and playerY == otherY:
        playerX = random.choice(range(0,2))
        playerY = random.choice(range(0,2))
    else:
        return playerX, playerY

  
def move_player(player, move):
  # Get the player's current location
  # If move is LEFT, y - 1
  # If move is RIGHT, y + 1
  # If move is UP, x - 1
  # If move is DOWN, x + 1
  return player


def get_moves(player):
  MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
  # if player's y is 0, remove LEFT
  # if player's x is 0, remove UP
  # if player's y is 2, remove RIGHT
  # if player's x is 2, remove DOWN
  return MOVES

while True:
  print("Welcome to the dungeon!")
  print("You're currently in room {}")  # fill in with player position
  print("You can move {}")  # fill in with available moves
  print("Enter QUIT to quit")
  
  move = input("> ")
  move = move.upper()
  
  if move == 'QUIT':
    break
    
  # If it's a good move, change the player's position
  # If it's a bad move, don't change anything
  # If the new player position is the door, they win!
  # If the new player position is the monster, they lose!
  # Otherwise, continue