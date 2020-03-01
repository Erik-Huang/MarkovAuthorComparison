import pandas as pd
import os

AUTHOR_LIST = [
    "Johnston, Mary",
    "Bacheller, Irving",
    "Hough, Emerson",
    "Doyle, Arthur Conan",
    "Parker, Gilbert",
    "Rice, Alice Caldwell Hegan",
    "Churchill, Winston",
    "Fox, John",
    "MacGrath, Harold",
    "Glasgow, Ellen",
    "McCutcheon, George Barr"
    ]

ROWS, COLS = (28, 28)

def main():
    resultList = open("./matricesPathList", "w+")
    for author in AUTHOR_LIST:
        print("Started on", author)
        fileList = getAllBooksForAuthor(author)
        for filePath in fileList:
            book = open(filePath, "r")
            text = book.read().lower()
            book.close()
            T = getTransMatrix(text, filePath)
            createCSV(filePath, T, resultList)
    resultList.close()


def getTransMatrix(text, filePath):
    T = [[0 for r in range(COLS)] for c in range(ROWS)]
    for i in range(1, len(text)):
    	next = getIndex(text[i])
    	prev = getIndex(text[i - 1])
    	T[prev][next] = T[prev][next] + 1
    for row in range(len(T)):
        rowSum = sum(T[row])
        if rowSum != 0:
        	for col in range(len(T[row])):
        		T[row][col] = T[row][col] / rowSum
        else:
            print("warning: zero sum row in", filePath)
    #print(T)
    return T

def getAllBooksForAuthor(author):
    filelist = []
    location = "./%s/" % reverseName(author)
    for i in os.scandir(location):
        if i.is_file() and i.path.endswith(".txt"):
            filelist.append(i.path)
    return filelist

def getIndex(c):
	if ord(c) >= ord('a') and ord(c) <= ord('z'):
		return ord(c) - ord('a')
	elif c == ' ' or c == '\n' or c == '\t':
		return 26
	else:
		return 27

def reverseName(author):
    author = author.split(", ")
    return author[1]+" "+author[0]

def createCSV(filePath, T, resultList):
    filePath = filePath.split("/")
    mtxDirPath = filePath[1] + " Matrices"
    os.system("mkdir " + mtxDirPath.replace(" ", "\ "))
    outputPath = "./%s/%s" % (mtxDirPath, filePath[1].replace(" ", ""))
    bookName = filePath[2].split(" ")
    for word in bookName:
        outputPath += word[0].upper()
    outputPath += ".csv"
    print("saving matrix result of", filePath[2])
    df = pd.DataFrame(data=T, columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "space", "symbol"])
    df.to_csv(outputPath, index=False, encoding='utf8')
    resultList.write(outputPath + "\n")

if __name__ == '__main__':
    main()
