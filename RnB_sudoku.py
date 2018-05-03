#global variable
grid_size = 81

def isFull(grid):
    return grid.count(0)==0

def getTrialCelli(grid):
    for i in range(grid_size):
        if grid[i] == 0:
            print('Trialling cell',i)
            return i

def isValid(trialVal, trialCelli, grid):
    cols=0
    #validate square
    for eachSq in range(9):
        trialSq = [ x+cols for x in range(3)]+\
                  [ x+9+cols for x in range(3)]+\
                  [ x+18+cols for x in range(3)]
        cols += 3
        if cols in [9,36]:
            cols += 18
        if trialCelli in trialSq:
            for i in trialSq:
                if grid[i] !=0:
                    if trialVal == int(grid[i]):
                        print('Square', end = "  ")
                        return False
    #validate row
    for eachRow in range(9):
        trialRow = [x+(9*eachRow) for x in range (9)]
        if trialCelli in trialRow:
            for i in trialRow:
                if grid[i] !=0:
                    if trialVal == int(grid[i]):
                        print('Row', end = "  ")
                        return False
    #validate column
    for eachCol in range(9):
        trialCol = [(9*x)+eachCol for x in range(9)]
        if trialCelli in trialCol:
            for i in trialCol:
                if grid[i]!=0:
                    if trialVal == int(grid[i]):
                        print('Column', end = "  ")
                        return False
    print('is Legal.','So, set cell',trialCelli,'with value',trialVal)
    return True

def setCell(trialVal, trialCelli, grid):
    grid[trialCelli] = trialVal
    return grid

def clearCell(trialCelli, grid):
    grid[trialCelli]=0
    print('Clear cell', trialCelli)
    return grid

def hasSolution(grid):
    if isFull(grid):
        print('\nSOLVED')
        return True
    else:
        trialCelli = getTrialCelli(grid)
        trialVal = 1
        solution_found = False
        while ( solution_found!= True) and (trialVal <10):
            print('Trial value', trialVal, end = "  ")
            if isValid(trialVal, trialCelli, grid):
                grid = setCell(trialVal, trialCelli, grid)
                if hasSolution(grid)==True:
                    solution_found = True
                    return True
                else:
                    clearCell(trialCelli, grid)
            print('++')
            trialVal +=1
    return solution_found
            
        
def printGrid (grid, add_zeros):
    i=0
    for val in grid:
        if add_zeros == 1:
            if int(val) < 10:
                print(0+str(val), end = "  ")
            else:
                print(val, end = "  ")
        else:
            print(val, end = "  ")
        i += 1
        if i in [(x*9)+3 for x in range(81)]+\
                 [(x*9)+6 for x in range(81)]+\
                 [(x*9)+9 for x in range(81)]:\
            print('|', end = "  ")
        if add_zeros == 1:
            if i in [27,54,81]:
                print('\n---------+---------+---------+')
            elif i in [(x*9) for x in range(81)]:
                print('\n')
        else:
            if i in [27,54,81]:
                print('\n----------+----------+----------+')
            elif i in [(x*9) for x in range(81)]:
                print('\n')
#sampleGrid = [ 0,6,0,4,0,7,0,0,3,
#                   3,4,2,0,0,5,6,0,0,
#                   1,9,7,6,8,3,2,5,4,
#                   0,8,0,1,3,2,0,0,0,
#                   7,0,0,0,0,8,0,0,2,
#                   2,0,0,7,6,4,5,0,0,
#                   0,2,0,0,0,1,3,4,0,
#                   0,0,0,3,4,9,0,0,0,
#                   0,0,0,2,0,6,8,9,0]
"""[ 0,0,0,4,2,0,0,0,0,
                   0,0,0,0,0,8,0,0,0,
                   0,0,0,0,6,1,9,0,8,
                   0,9,0,0,3,0,0,5,0,
                   2,0,0,0,0,0,0,9,6,
                   7,5,3,1,0,6,0,0,0,
                   0,0,0,0,0,0,0,0,1,
                   0,2,7,0,0,0,5,4,0,
                   5,0,0,9,8,0,0,7,2]"""

def main():
    sampleGrid = [ 1,8,5,4,2,9,7,6,3,
                   9,6,2,3,7,8,4,1,5,
                   3,7,4,0,6,1,9,2,8,
                   0,9,6,0,3,0,1,5,7,
                   2,1,8,0,0,0,3,9,6,
                   7,5,3,1,0,6,2,8,4,
                   6,4,9,2,5,7,8,3,1,
                   0,2,7,6,1,3,5,4,0,
                   5,0,0,9,8,4,6,7,2]
    printGrid(sampleGrid,0)
    if hasSolution (sampleGrid):
        printGrid(sampleGrid, 0)
    else:
        print('NO SOLUTION')
            

if __name__ == "__main__":
    main()
            
