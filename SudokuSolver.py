from utility import getBlock, getBox, getNumber, getVarNumber
from display import displaySol
import displayGUI
import sys, os
import subprocess

file = open("SudokuSolution.cnf", mode='w')

puzzle = [
         [8,0,0,0,0,3,0,7,0],
         [0,0,0,6,0,0,0,9,0],
         [0,0,0,0,0,0,2,0,0],
         [0,5,0,0,0,0,0,0,0],
         [0,0,7,0,4,5,1,0,0],
         [0,0,0,7,0,0,0,3,0],
         [0,0,1,0,0,8,0,9,0],
         [0,0,0,5,0,0,0,0,0],
         [0,6,8,0,1,0,4,0,0]
         ]
print()
print("hackrush sudoku solver")
print("       SUDOKU\n")
for i in range(3):
    for row in range(3):
        for blk in range(3*i, 3*(i+1)):
            for col in range(3):
                if puzzle[blk][row*3 + col] == 0:
                    print('-', end = ' ')
                else:
                    print(puzzle[blk][row*3 + col], end=' ')
            if (blk + 1)%3 != 0:
                print('| ', end = '')
        print()

    if (i + 1)%3 != 0:
        print("------+-------+-------")

# puzzle = inputGUI()

def main():

    global file


    # navigating block wise
    for block in range(9):

        # checks each box
        for box in range(9):
            
            varNumber = getVarNumber(block, box, puzzle[block][box])   # gets the SAT variable associated with the number

            # if a number already exists in the box then row, col, and block constraints are output
            if (puzzle[block][box] != 0):
                file.write("{0:d} 0\n".format(varNumber))   # and writes it (+ve signifying true)

                # writes -ve constraints
                getCols(varNumber)
                getRows(varNumber)
                getBlocks(varNumber)
            # else writes all the SAT variables as +ve in one clause as at least one should be true
            else:

                #  all the variables
                for i in range(9):
                    var = 81*block + 9*box + i + 1
                    file.write("{0:d} ".format(var))
                file.write("{0:d}\n".format(0))

                for i in range(9):
                    var = 81*block + 9*box + i + 1
                    getCols(var)
                    getRows(var)
                    getBlocks(var)

    file.close()
    nullOut = open(os.devnull, "w")
    subprocess.call(['minisat', 'SudokuSolution.cnf', 'SudokuSolution.sol'], stdout=nullOut)
    solution = displaySol()
    displayGUI.outputGUI(solution)
    

# gets the SAT variable numbers in the same column
def getCols(varNumber):
    
    global file

    # gets the block, box and number associated with the SAT varNumber
    block = getBlock(varNumber)
    box = getBox(varNumber)
    number = getNumber(varNumber)

    colIndex = box % 3     # only 3 columns in a block, so mod 3 to get the column index from box number
    prevBlock = block - 3  # starts with the block 3-before the current block
    nextBlock = block + 3  # starts with the block 3-after the current block

    # writes the SAT vars in the same column of the prev blocks
    while(prevBlock >= 0):

        # checks for each box(=i)
        for i in range(9):

            # writes if in the same column and is blank
            if(i%3 == colIndex and puzzle[prevBlock][i] == 0):
                file.write("-{0:d} -{1:d} 0\n".format(varNumber,getVarNumber(prevBlock, i, number)))

        prevBlock = prevBlock - 3    # decreases the block by 3

    # writes the SAT vars in the same column of the next blocks
    while(nextBlock <= 8):

        # checks for each box
        for i in range(9):

            # writes if in the same column and is blank
            if(i%3 == colIndex and puzzle[nextBlock][i] == 0):
                file.write("-{0:d} -{1:d} 0\n".format(varNumber,getVarNumber(nextBlock, i, number)))

        nextBlock = nextBlock + 3


# gets the SAT variable numbers in the same row
def getRows(varNumber):
    # gets the block, box and number associated with the SAT varNumber
    block = getBlock(varNumber)
    box = getBox(varNumber)
    number = getNumber(varNumber)

    rowIndex = int(box / 3)  # only 3 rows in a block, so divided by 3 to get the row index from box number
    prevBlock = block        # starts with the current block
    nextBlock = block        # starts with the current block

    # writes the SAT vars in the same row of the prev blocks
    while(prevBlock % 3 != 0):
        prevBlock = prevBlock - 1

        # checks for each box
        for i in range(9):

            # writes if in the same row and is blank
            if(int(i/3) == rowIndex and puzzle[prevBlock][i] == 0):
                # write(prevBlock, i, number)
                file.write("-{0:d} -{1:d} 0\n".format(varNumber,getVarNumber(prevBlock, i, number)))

    # writes the SAT vars in the same row of the next blocks
    while(nextBlock % 3 != 2):
        nextBlock = nextBlock + 1
        
        # checks for each box
        for i in range(9):

            # writes if in the same column and is blank
            if(int(i/3) == rowIndex and puzzle[nextBlock][i] == 0):
                # write(nextBlock, i, number)
                file.write("-{0:d} -{1:d} 0\n".format(varNumber,getVarNumber(nextBlock, i, number)))


# gets the SAT variable numbers in the same block
def getBlocks(varNumber):
    # gets the block, box and number associated with the SAT varNumber
    block = getBlock(varNumber)
    box = getBox(varNumber)
    number = getNumber(varNumber)

    # checks for each box
    for i in range(9):

        # writes if even if it is NOT blank as that leads to problems when the last box is already filled
        # it doesn't generate the variables for the ones that are already input, and that may lead to missing
        # cnf clauses(the code that worked before this was just luck I guess)
        if(i != box):
            # write(block, i,number)
            file.write("-{0:d} -{1:d} 0\n".format(varNumber,getVarNumber(block, i, number)))


if __name__ == '__main__':
    main()