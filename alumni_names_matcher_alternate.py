import xlrd
import csv
from time import time

def makeBuckets(rows):
    dic = {}
    for name in rows:
        insertName(name, dic)

    return dic

def insertName(name, dic):
    if(name == ''):
        return

    first_letter = name[0]

    if(first_letter in dic):
        insertName(name[1:], dic[first_letter])
        return
    else:
        dic[first_letter] = {}
        insertName(name[1:], dic[first_letter])
        return

def checkInBuckets(dic, name):
    if(name == ''):
        return True
    else:
        letter = name[0]
        if(letter in dic):
            return checkInBuckets(dic[letter], name[1:])
        else:
            return False


def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

def loadFromExcel(excelFile):
    allRows = []
    book = xlrd.open_workbook(excelFile)
    for sheet in book.sheets():
        for row in range(sheet.nrows):
            allRows.append(sheet.row(row))

    return allRows

def nameMatch(alumniNames, muslimNames):
    matches = []
    muslimDic = makeBuckets(muslimNames)

    for row in alumniNames:
        """if (binarySearch(muslimNames, row[1].value.split(' ')[0])):"""
        name = row[1].value.split(' ')[0]
        if(checkInBuckets(muslimDic, name)):
            matches.append([unicode(c.value).encode('utf-8') for c in row])
        """for colidx, cell in enumerate(row):
            if colidx == 1:
                for name in muslimNames:
                    firstName = cell.value.split(" ")[0]
                    if(firstName == name):
                        #print row
                        matches.append(row)"""

    return matches

with open('names.txt') as f:
    content = f.readlines()

muslimNames = sorted([x.strip('\n') for x in content])
muslimNames.append("Abdul")
#muslimNames = ["Abdul"]

alumniNames = loadFromExcel('ubisoc 2010_2016_Final.xlsx')
t0 = time()
matches = nameMatch(alumniNames, muslimNames)
t1 = time()

print "Time: " + "{:.9f}".format((t1-t0))
#print matches
print len(matches)

with open('output.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(matches)
