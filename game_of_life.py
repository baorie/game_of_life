import time, curses, os
import numpy as np
import random as rd

TERMINAL_SIZE = os.get_terminal_size()

def dead_state(width, height):
    return np.zeros(shape=(width,height), dtype= int)

def random_state(width, height):
    # Build the board using your previous work
    state = dead_state(width, height)
    r, c = state.shape[0], state.shape[1]

    # TODO: randomize each element of 'state' to either 0 or 1
    for i in range(r):
        for j in range(c):
            rd_num = rd.random()
            if rd_num >= 0.5:
                state[i,j] = 0
            else:
                state[i,j] = 1
    return state

def render(state):
    r, c = state.shape[0], state.shape[1]
    table = ""
    for i in range(r):
        row = ""
        for j in range(c):
            if state[i,j] == 0:
                row += chr(9617) + chr(9617)
            elif state[i,j] == 1:
                row += chr(9608) + chr(9608)
        if not (i == r-1):
            table = table + row + "\n"
        else:
            table = table + row
    return table

def next_board_state(og_state):
    """ RULES OF LIFE
    1. UNDERPOPULATION: Any live cell with 0 or 1 live neighbors becomes dead
    2. PERFECT: Any live cell with 2 or 3 live neighbors stays alive
    3. OVERPOPULATION: Any live cell with > 3 live neighbors becomes dead
    4. REPRODUCTION: Any dead cell with exactly 3 live neighbors becomes alive
    """

    r, c = og_state.shape[0], og_state.shape[1]
    new_state = dead_state(r, c)
    for i in range(r):
        for j in range(c):
            cell = og_state[i,j]
            dead_neighbors = 0
            alive_neighbors = 0
            if (i > 0) and (i < r-1) and (j > 0) and (j < c-1):
                # Process normal cases
                nb_0 = og_state[i-1,j-1] 
                nb_1 = og_state[i-1,j]
                nb_2 = og_state[i-1,j+1]
                nb_3 = og_state[i,j-1]
                nb_4 = og_state[i,j+1]
                nb_5 = og_state[i+1,j-1]
                nb_6 = og_state[i+1,j]
                nb_7 = og_state[i+1,j+1]
                nb_normal = [nb_0, nb_1, nb_2, nb_3, nb_4, nb_5, nb_6, nb_7]
                for k in nb_normal:
                    if k == 0:
                        dead_neighbors = dead_neighbors + 1
                    elif k == 1:
                        alive_neighbors = alive_neighbors + 1
                if cell == 1: #alive
                    if alive_neighbors < 2: #underpopulation
                        new_state[i,j] = 0
                    elif alive_neighbors > 1 and alive_neighbors < 4: #perfect
                        new_state[i,j] = 1
                    elif alive_neighbors > 3: # overpopulation
                        new_state[i,j] = 0
                elif cell == 0 and alive_neighbors == 3: # reproduction
                    new_state[i,j] = 1
            elif (i == 0) and (j > 0) and (j < c-1): #north edge
                nb_0 = og_state[i,j-1] 
                nb_1 = og_state[i,j+1]
                nb_2 = og_state[i+1,j-1]
                nb_3 = og_state[i+1,j]
                nb_4 = og_state[i+1,j+1]
                nb_north = [nb_0, nb_1, nb_2, nb_3, nb_4]
                for k in nb_north:
                    if k == 0:
                        dead_neighbors = dead_neighbors + 1
                    elif k == 1:
                        alive_neighbors = alive_neighbors + 1
                if cell == 1: #alive
                    if alive_neighbors < 2 : #underpopulation
                        new_state[i,j] = 0
                    elif alive_neighbors > 1 and alive_neighbors < 4: #perfect
                        new_state[i,j] = 1
                    elif alive_neighbors > 3: # overpopulation
                        new_state[i,j] = 0
                elif cell == 0 and alive_neighbors == 3: # reproduciton
                    new_state[i,j] = 1
            elif (i == r-1) and (j > 0) and (j < c-1): #south edge
                nb_0 = og_state[i-1,j-1]
                nb_1 = og_state[i-1,j]
                nb_2 = og_state[i-1,j+1]
                nb_3 = og_state[i,j-1]
                nb_4 = og_state[i,j+1]
                nb_south = [nb_0, nb_1, nb_2, nb_3, nb_4]
                for k in nb_south:
                    if k == 0:
                        dead_neighbors = dead_neighbors + 1
                    elif k == 1: 
                        alive_neighbors = alive_neighbors + 1
                if cell == 1: #alive
                    if alive_neighbors < 2: #underpopulation
                        new_state[i,j] = 0
                    elif alive_neighbors > 1 and alive_neighbors < 4: #perfect
                        new_state[i,j] = 1
                    elif alive_neighbors > 3: # overpopulation
                        new_state[i,j] = 0
                elif cell == 0 and alive_neighbors == 3: #reproduction
                    new_state[i,j] = 1
            elif (i > 0) and (i < r-1) and (j == c-1): #east
                nb_0 = og_state[i-1,j-1]
                nb_1 = og_state[i-1,j]
                nb_2 = og_state[i,j-1]
                nb_3 = og_state[i+1,j-1]
                nb_4 = og_state[i+1,j]
                nb_east = [nb_0, nb_1, nb_2, nb_3, nb_4]
                for k in nb_east:
                    if k == 0:
                        dead_neighbors = dead_neighbors + 1
                    elif k == 1:
                        alive_neighbors = alive_neighbors + 1
                if cell == 1: #alive
                    if alive_neighbors < 2: #underpopulation
                        new_state[i,j] = 0
                    elif alive_neighbors > 1 and alive_neighbors < 4: #perfect
                        new_state[i,j] = 1
                    elif alive_neighbors > 3: #overpopulation
                        new_state[i,j] = 0
                elif cell == 0 and alive_neighbors == 3: #reproduction
                    new_state[i,j] = 1
            elif (i > 0) and (i < r-1) and (j == 0): #west
                nb_0 = og_state[i-1,j]
                nb_1 = og_state[i-1,j+1]
                nb_2 = og_state[i,j+1]
                nb_3 = og_state[i+1,j]
                nb_4 = og_state[i+1, j+1]
                nb_west = [nb_0, nb_1, nb_2, nb_3, nb_4]
                for k in nb_west:
                    if k == 0:
                        dead_neighbors = dead_neighbors + 1
                    elif k == 1:
                        alive_neighbors = alive_neighbors + 1
                if cell == 1: #alive
                    if alive_neighbors < 2: #underpopulation
                        new_state[i,j] = 0
                    elif alive_neighbors > 1 and alive_neighbors < 4: #perfect
                        new_state[i,j] = 1
                    elif alive_neighbors > 3: #overpopulation
                        new_state[i,j] = 0
                elif cell == 0 and alive_neighbors == 3: #reproduction
                    new_state[i,j] = 1
            elif (i == 0) and (j == 0): #nw corner
                nb_0 = og_state[i,j+1]
                nb_1 = og_state[i+1,j+1]
                nb_2 = og_state[i+1,j]
                nb_nw = [nb_0, nb_1, nb_2]
                for k in nb_nw:
                    if k == 0:
                        dead_neighbors = dead_neighbors + 1
                    elif k == 1:
                        alive_neighbors = alive_neighbors + 1
                if cell == 1: #alive
                    if alive_neighbors < 2: #underpopulation
                        new_state[i,j] = 0
                    elif alive_neighbors > 1 and alive_neighbors < 4: #perfect
                        new_state[i,j] = 1
                    elif alive_neighbors > 3: #overpopulation
                        new_state[i,j] = 0
                elif cell == 0 and alive_neighbors == 3: #reproduction
                    new_state[i,j] = 1
            elif (i == 0) and (j == c-1): #ne corner
                nb_0 = og_state[i,j-1]
                nb_1 = og_state[i+1,j-1] 
                nb_2 = og_state[i+1,j]
                nb_ne = [nb_0, nb_1, nb_2]
                for k in nb_ne:
                    if k == 0:
                        dead_neighbors = dead_neighbors + 1
                    elif k == 1:
                        alive_neighbors = alive_neighbors + 1
                if cell == 1: #alive
                    if alive_neighbors < 2: #underpopulation
                        new_state[i,j] = 0
                    elif alive_neighbors > 1 and alive_neighbors < 4: #perfect
                        new_state[i,j] = 1
                    elif alive_neigbors > 3: #overpopulation
                        new_state[i,j] = 0
                elif cell == 0 and alive_neighbors == 3: #reproduction
                    new_state[i,j] = 1
            elif (i == r-1) and (j == 0): #sw corner
                nb_0 = og_state[i-1,j]
                nb_1 = og_state[i-1,j+1]
                nb_2 = og_state[i,j+1]
                nb_sw = [nb_0, nb_1, nb_2]
                for k in nb_sw:
                    if k == 0:
                        dead_neighbors = dead_neighbors + 1
                    elif k == 1:
                        alive_neighbors = alive_neighbors + 1
                if cell == 1: #alive
                    if alive_neighbors < 2: #underpopulation
                        new_state[i,j] = 0
                    elif alive_neighbors > 1 and alive_neighbors < 4: #perfect
                        new_state[i,j] = 1
                    elif alive_neighbors > 3: #overpopulation
                        new_state[i,j] = 0
                elif cell == 0 and alive_neighbors == 3: #reproduction
                    new_state[i,j] = 1
            elif (i == r-1) and (j == c-1): #se corner
                nb_0 = og_state[i,j-1]
                nb_1 = og_state[i-1,j-1]
                nb_2 = og_state[i-1,j]
                nb_se = [nb_0, nb_1, nb_2]
                for k in nb_se:
                    if k == 0:
                        dead_neighbors = dead_neighbors + 1
                    elif k == 1:
                        alive_neighbors = alive_neighbors + 1
                if cell == 1: #alive
                    if alive_neighbors < 2: #underpopulation
                        new_state[i,j] = 0
                    elif alive_neighbors > 1 and alive_neighbors < 4: #perfect
                        new_state[i,j] = 1
                    elif alive_neighbors > 3: #overpopulation
                        new_state[i,j] = 0
                elif cell == 0 and alive_neighbors == 3: #reproduction
                    new_state[i,j] = 1
    return new_state

if  __name__ == "__main__":

    board_height = int(input("Please enter a board height less than or equal to " + str(TERMINAL_SIZE.columns//2)+ ": "))
    board_width = int(input("Please enter a board width less than or equal to " + str(TERMINAL_SIZE.lines) +": "))
    prev_state = random_state(board_width, board_height)
    stdscr = curses.initscr()
    i = 0
    while(i < 30):
        next_state = next_board_state(prev_state)
        prev_state = next_state
        stdscr.addstr(0,0, render(next_state))
        stdscr.refresh()
        time.sleep(0.25)
        i = i + 1
