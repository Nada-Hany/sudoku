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
    found = False
    file_path = ""
    for root, dirs, files in os.walk(startDir):
        if path in files:
            found = True
            file_path = os.path.join(root, path)
            break
    # Open the file if found
    if found:
        return file_path
    return None