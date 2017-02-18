# gets the index of the big 3x3 block
def getBlock(varNumber):
    block = int((varNumber - 1) / 81) # varNumber - 1 is done to account for the corner cases
                                      # such as 81 should be in block 0 not 1, as the variables are 1-indexed
    # print("Block Index Is: {0:d}".format(block))
    return block


# gets the index of the small 1x1 box inside the big 3x3 block
def getBox(varNumber):
    localVarIndex = (varNumber - 1) % 81 # returns the variable index w.r.t. 3x3 block, varNumber-1 for corner cases
    box = int((localVarIndex) / 9)
    # print("Box Index Is: {0:d}".format(box))
    return box


# gets the number associated with the variable number
def getNumber(varNumber):
    number = (varNumber - 1) % 9
    number = number + 1
    # print("Number is: {0:d}".format(number))
    return number


# get the SAT variable number from block, box and number
def getVarNumber(block, box, number):
    varNumber = 81*block + 9*box + number
    # print("Variable Number is: {0:d}".format(varNumber))
    return varNumber


# changes the grid position to the positions required by the puzzle(i.e. block,box and number)
def getPuzzlePos(row, column, number):
    block = int(row / 3) * 3 + int(column / 3)
    box = int(row % 3) * 3 + int(column % 3)
    return block, box, number
