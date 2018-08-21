from game_of_life import next_board_state, dead_state

if  __name__ == "__main__":

    """
    Writing tests within main script

    TEST 1: dead cells with no live neighbors should stay dead
    """
    init_state1 = dead_state(3,3)
    expected_next_state1 = dead_state(3,3)
    actual_next_state1 = next_board_state(init_state1)

    if (expected_next_state1 == actual_next_state1).all():
        print("PASSED 1")
        print("Expected:")
        print(expected_next_state1)
        print("Actual: ")
        print(actual_next_state1)
    else:
        print("FAILED 1!")
        print("Expected:")
        print(expected_next_state1)
        print("Actual: ")
        print(actual_next_state1)
    """
    TEST 2: dead cells with exactly 3 neighbors should come alive
    """
    init_state2 = dead_state(3,3)
    init_state2[0,2] = 1
    init_state2[1,1] = 1
    init_state2[1,2] = 1
    expected_next_state2 = dead_state(3,3)
    expected_next_state2[0,1] = 1
    expected_next_state2[0,2] = 1
    expected_next_state2[1,1] = 1
    expected_next_state2[1,2] = 1
    actual_next_state2 = next_board_state(init_state2)
    
    if (expected_next_state2 == actual_next_state2).all(): 
        print("PASSED 2")
        print("Expected:")
        print(expected_next_state2)
        print("Actual: ")
        print(actual_next_state2)
    else:
        print("FAILED 2!")
        print("Expected:")
        print(expected_next_state2)
        print("Actual:")
        print(actual_next_state2)
    """
    TEST 3: live cells die when they have more than three live neighbors
    """
    init_state3 = dead_state(3,3)
    init_state3[0,0] = 1
    init_state3[0,1] = 1
    init_state3[0,2] = 1
    init_state3[1,1] = 1
    init_state3[1,2] = 1
    expected_next_state3 = dead_state(3,3)
    expected_next_state3[0,0] = 1
    expected_next_state3[1,0] = 1
    expected_next_state3[0,2] = 1
    expected_next_state3[1,2] = 1
    actual_next_state3 = next_board_state(init_state3)
    if (expected_next_state3 == actual_next_state3).all():
        print("PASSED 3")
    else: 
        print("FAILED 3!")
        print("Expected:")
        print(expected_next_state3)
        print("Actual:")
        print(actual_next_state3)
