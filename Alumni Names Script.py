import xlrd

def loadFromExcel(excelFile):
    allRows = []
    book = xlrd.open_workbook(excelFile)  
    for sheet in book.sheets():
        for row in range(sheet.nrows):    
            allRows.append(sheet.row(row))

    return allRows

def nameMatch(alumniNames, muslimNames):
    matches = []
    for row in alumniNames:
        for colidx, cell in enumerate(row):
            if colidx == 1:
                for name in muslimNames:
                    firstName = cell.value.split(" ")[0]
                    if(firstName == name):
                        print row
                        matches.append(row)

    return matches

muslimNames = [
        "Abdi"
    ]

alumniNames = loadFromExcel('ubisoc 2010_2016_Final.xlsx')
matches = nameMatch(alumniNames, muslimNames)
