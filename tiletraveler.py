import random
# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'
YES = 'y'
NO = 'n'
levers = [(1,2), (2,2), (2,3), (3,2)]
def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def play_one_move(col, row, valid_directions, total_coins):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = random.choice([NORTH, EAST, SOUTH, WEST])
    direction = direction.lower()
    print("Destinations: {}".format(direction))
    
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        lever_pulled = lever_pull(col, row)
        victory = is_victory(col, row)
        total_coins += lever_pulled
        if lever_pulled == 1:
            print("You received 1 coin, your total is now {}.".format(total_coins))
    return victory, col, row, total_coins

def lever_pull(x, y):
    a_tuple = (x, y)
    if a_tuple in levers:
        choice = random.choice([YES, NO])
        choice = choice.lower()
        print("Pull a lever (y/n): {}".format(choice))
        if choice == "y":
            return 1
        else:
            return 0
    else:
        return 0
    
def retry():
    retry = input("Play again (y/n): ")
    retry = retry.lower()
    if retry == "y":
        main()
        
# The main program starts here
def main():
    victory = False
    row = 1
    col = 1
    total_coins = 0
    seed_input = int(input("Input seed: "))
    random.seed(seed_input)
    random.choice([YES, NO])
    random.choice([NORTH, EAST, SOUTH, WEST])

    while not victory:
        valid_directions = find_directions(col, row)
        copy_place = row, col
        print_directions(valid_directions)
        victory, col, row, total_coins = play_one_move(col, row, valid_directions, total_coins)
    print("Victory! Total coins {}.".format(total_coins))
    retry()

main()
