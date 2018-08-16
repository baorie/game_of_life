import numpy as np
import random as rd

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
    for i in range(r):
        row = ""
        for j in range(c):
            if state[i,j] == 0:
                row += chr(9617) + chr(9617)
            elif state[i,j] == 1:
                row += chr(9608) + chr(9608)
        print(row)

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
                nb_4 = og_state[i,j]
                nb_5 = og_state[i,j+1]
                nb_6 = og_state[i+1,j-1]
                nb_7 = og_state[i+1,j]
                nb_8 = og_state[i+1,j+1]
                nb = [nb_0, nb_1, nb_2, nb_3, nb_4, nb_5, nb_6, nb_7, nb_8]
                for k in nb:
                    if k == 0:
                        dead_neighbors = dead_neighbors + 1
                    elif k == 1:
                        alive_neighbors = alive_neighbors + 1
                if cell == 1: #alive
                    if alive_neighbors < 2: #underpopulation
                        new_state[i,j] = 0
                    elif alive_neighbors > 1 and alive_neighbors < 4: #perfect
                        new_state[i,j] = 1
                    elif alive_neighbors > 3:
                        new_state[i,j] = 0
                elif cell == 0 and alive_neighbors == 3:
                    new_state[i,j] = 1
            else:
                # Process (literal) edge cases
    return new_state

if  __name__ == "__main__":
    board_width = int(input("Please enter a board width: "))
    board_height = int(input("Please enter a board height: "))
    example = random_state(board_width, board_height)
    print(example)
    render(example)
