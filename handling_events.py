from file import *
import sudoku


def event_loop():
    print("1- Read sudoku file.")
    print("2- Play a game")
    print("3- Continue playing last game")
    print("4- Exist game")
    ans = input("Enter the corresponding number for the operation you want: \n")
    if (ans == "1"):
        get_sudoku()
    elif (ans == "4"):
        return True
    else:
        print("Please enter a valid option.")
        event_loop()

def get_sudoku():
    ans = input("Enter file name with the write format for your desired sudoku: \n"
                +"Write 'back' if you want to do another operation\n")
    if(ans.lower() == "back"):
        event_loop()
    file = getFile(ans)
    if(file == None):
        print("file doesn't exist please try again")
        get_sudoku()
    else:
        print("file found successfully")
    map = sudoku.Sudoku()
    list = readStructure(file)
    map.initalizeSudoku(list)
    return map

