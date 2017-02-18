from utility import getNumber
import sys


def displaySol():
    file = open("SudokuSolution.sol", mode='r').read().splitlines()

    '''
    instead of doing this:
    puzzle=[[],[],[],[],[],[],[],[],[]]

    we can use this, list comprehension
    (Creates a list containing 5 lists, each of 8 items, all set to 0):

    w, h = 8, 5. 
    Matrix = [[0 for x in range(w)] for y in range(h)]
    '''
    puzzle = [[] for _ in range(9)]

    if file[0] == 'SAT':
        result = file[1].split()
        print(len(result))


        for i in range(729):
            if int(result[i]) > 0:
                number = getNumber(int(result[i]))
                puzzle[int(i/81)].append(number)

        # outputGUI(puzzle)
        print("\n      SOLUTION\n")
        for i in range(3):
            for row in range(3):
                for blk in range(3*i, 3*(i+1)):
                    for col in range(3):
                        print(puzzle[blk][row*3 + col], end=' ')
                    if (blk + 1)%3 != 0:
                        print('| ', end = '')
                print()

            if (i + 1)%3 != 0:
                print("------+-------+-------")
    else:
        print("Unsolvable or wrong Sudoku")

    return puzzle