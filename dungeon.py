import random 
'''Written by Tara Edwards for Treehouse'''
'''Uses random.choice for two lists of a range between 0 and 2'''

CELLS = [(0,0), (0,1), (0,2),
        (1,0), (1,1), (1,2),
        (2,0), (2,1), (2,2)]
#a list of tuples

def draw_map():
    print("__")
    tile = '|{}'
    for idx, cell in enumerate(CELLS):
        if idx in [0, 1, 3, 4, 6, 7]:
            if cell == player:
                print(tile.format('X'), end='')
    
            else:
                print(tile.format('_'), end='')
       
        else:
            if cell == player:
                print(tile.format('X|'))
            else:
                print(tile.format('_|'))

def get_locations():
# monster = random
    monster_coord = random.choice(CELLS)
# door = random
    door_coord = random.choice(CELLS)
# start = random
    start_coord = random.choice(CELLS)
# if monster, door, or start are the same, do it again
    if monster_coord == door_coord or monster_coord == start_coord or door_coord == start_coord:
        return get_locations() 
    return monster_coord, door_coord, start_coord 


def move_player(player, move): 
# Get the player's current location
#player  = x, y
    x, y = player 
# If move is LEFT, y - 1
    if move == "LEFT":
        y -= 1
# If move is RIGHT, y + 1
    elif move == "RIGHT":
        y += 1
# If move is UP, x - 1
    elif move == "UP":
        x -= 1
# If move is DOWN, x + 1
    elif move == "DOWN":
        x += 1   
    return x, y


def get_moves(player):
#player = x, y 
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
# if player's y is 0, remove LEFT
    if player[1] == 0:
        moves.remove("LEFT")
# if player's y is 2, remove RIGHT
    if player[1] == 2:
        moves.remove("RIGHT")
# if player's x is 0, remove UP
    if player[0] == 0:
        moves.remove("UP")
# if player's x is 2, remove DOWN
    if player[0] == 2:
        moves.remove("DOWN") 
    return moves

monster, door, player = get_locations()
print("Welcome to the dungeon!")

while True:
    moves = get_moves(player) 
    print("You're currently in room {}")  # fill in with player position
    print("You can move {}".format(moves))  # fill in with available moves
    print("Enter QUIT to quit")
  
    move = input("> ")
    move = move.upper()
  
    if move == 'QUIT':
        break

# If it's a good move, change the player's position
    if move in moves:
        player = move_player(player, move)
#change player to x, y? 
#no, player = a tuple returned from the function 
# If it's a bad move, don't change anything
    else:
        print("Walls are hard. Stop walking into them. ") 
        continue

# If the new player position is the door, they win!
    if player == door:
        print("You found your way out of the maze! ")
        break
    elif player == monster:
        print("You were eaten by the grue. ")
        break 
#I typed the same joke before making changes
#Are nerds that predictable? Yes 
# If the new player position is the monster, they lose!
# Otherwise, continue
#Change your player to a dictionary with a key that holds onto where the player has been. Then, when drawing the map, show . for every cell they've been in.
