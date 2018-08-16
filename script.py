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

if  __name__ == "__main__":
    board_width = int(input("Please enter a board width: "))
    board_height = int(input("Please enter a board height: "))
    example = random_state(board_width, board_height)
    print(example)
