import sudoku
from file import *


map = sudoku.Sudoku()

# map.changeValue(0, 2, 1)
# map.changeValue(0, 6, 8)
# map.changeValue(1, 1, 3)
# map.changeValue(1, 8, 2)
# map.changeValue(2, 0, 4)
# map.changeValue(2, 7, 9)
# map.changeValue(3, 3, 2)
# map.changeValue(3, 8, 7)
# map.changeValue(4, 1, 8)
# map.changeValue(4, 4, 1)
# map.changeValue(4, 6, 6)
# map.changeValue(5, 0, 5)
# map.changeValue(5, 4, 3)
# map.changeValue(5, 5, 9)
# map.changeValue(6, 4, 6)
# map.changeValue(6, 6, 1)
# map.changeValue(7, 1, 2)
# map.changeValue(7, 5, 5)
# map.changeValue(7, 8, 3)
# map.changeValue(8, 2, 7)
# map.changeValue(8, 3, 8)
# map.changeValue(8, 7, 4)


map.changeValue(0, 1, 4)
map.changeValue(0, 2, 6)
map.changeValue(0, 4, 2)
map.changeValue(0, 7, 9)


# print(map.display())
# print(10*"-")
# check = False
# # if map.validSudoku:
# check = map.solveSudoku(0, 0)

# print(check)
# print(map.display())

file = open("structure.txt", "r")
# check = readStructure("structure.txt")
# print(check)

wantedFile = getFile("test__test.txt")
print(wantedFile)
check = readStructure(wantedFile)
print(check)