import cell

class Sudoku:
    def __init__(self) -> None:
       self.size = 9
    #   self.CELLWIDTH= CELLWIDTH
    #    self.XOFFSET = XOFFSET
    #    self.YOFFSET = YOFFSET
       self.map =[[cell.Cell(x, y) for x in range (9)] for y in range (9)]
    
    # def __init__(self) -> None:
    #     self.map =[[cell.Cell(x, y) for x in range (9)]for y in range (9)]

    
    def getSudoku(self):
        return self.map

    def changeValue(self, x, y, value):
        self.map[x][y].value = value
        self.map[x][y].isFixed = True

    def getValue(self, x, y):
        return self.map[x][y].value

    def validRow(self, x, value):
        for i in range(9):
            if (self.map[x][i].value == value):
                return False
        return True

    def validCol(self, y, value):
        for i in range(9):
            if (self.map[i][y].value == value):
                return False
        return True

    def validBox(self, x, y, value):
        rowOFF = x - x%3
        colOFF = y - y%3    

        for i in range(3):  
            for j in range(3): 
                if(self.map[i+rowOFF][j+colOFF].value == value):
                    return False
                
        return True

    def validMove(self, x, y, value):
        if(self.validBox(x, y, value) and self.validCol(y, value) and self.validRow(x, value)):
            return True
        return False

    def validSudoku(self):
        isValid = True
        for i in range(9):  
            for j in range(9): 
                if self.map[i][j].value != 0:
                    isValid = self.validBox(i, j, self.map[i][j].value) and self.validCol(j, self.map[i][j].value) and self.validRow(i, self.map[i][j].value)
                if not isValid:
                    return False
        return True
                

    def solveSudoku(self, row, col):
        # time to check for next row
        if(col == self.size):
            col = 0
            row += 1
        # finished all cells -- base case
        if (row == self.size):
            return True
        # iterating over all possible values [1-9]
        for i in range(1, 10):
            # valid number
            if (self.validMove(row, col, i) and self.map[row][col].isFixed == False):
                self.map[row][col].value = i
            
                # return true when all cells are finished and valid
                if(self.solveSudoku(row, col + 1)):
                    return True
            # all numbers are invalid 
            if not self.map[row][col].isFixed:
                self.map[row][col].value = 0
        # returns false when a cell is invalid with all possible values and time to move back
        return False


    def display(self):
        for row in self.map:
            for element in row:
                print(f"{element.value}  ", end=" ")
            print() 
