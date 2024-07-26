import os

def readStructure(fileName):
    list = []
    file = open(fileName, "r")
    for line in file:
        row = []
        for cell in line.split():
            row.append(cell.strip())
        list.append(row)
    return list

def getFile(path):
    startDir = "C:/"
    for root, dirs, files in os.walk(startDir):
        if path in files:
            file_path = os.path.join(root, path)
            break
    # Open the file if found
    if file_path:
        return file_path
    return None