class Cell:
    
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
        self.isSelected = False
        self.value = 0
        self.isFixed = False
        # self.XOFFSET = XOFFSET 
        # self.YOFFSET = YOFFSET
        # self.x = self.XOFFSET+ self.CELLWIDTH * self.row
        # self.y = self.YOFFSET + self.CELLWIDTH * self.col