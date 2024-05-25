def readStructure(fileName, list):
    file = open(fileName, "r")
    for line in file:
        row = []
        for cell in line.split():
            row.append(cell.strip())
        list.append(row)


def constructSudoku(list):
    pass