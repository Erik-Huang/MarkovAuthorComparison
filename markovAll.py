import pandas as pd
import os

AUTHOR_LIST = [
    "Johnston, Mary",
    "Bacheller, Irving",
    "Hough, Emerson",
    "Doyle, Arthur Conan",
    "Parker, Gilbert",
    "Rice, Alice Caldwell Hegan",
    "Fox, John",
    "MacGrath, Harold",
    "Glasgow, Ellen",
    "McCutcheon, George Barr"
    ]


ROWS, COLS = (28, 28)

def main():
    matricesPathList = open("./matricesPathList.txt", "w+")
    genAllMatrices(matricesPathList)
    matricesPathList.close()

# Generate matrices for each book and all books for an author
def genAllMatrices(matricesPathList):
    for author in AUTHOR_LIST:
        print("Started on", author)
        fullText = "";
        fileList = getAllBooksForAuthor(author)
        folderDirectory = fileList[0].split("/")[1] + " Matrices"
        os.system("mkdir " + folderDirectory.replace(" ", "\ "))
        for filePath in fileList:
            book = open(filePath, "r")
            text = book.read().lower()
            fullText += text
            book.close()
            T = getTransMatrix(text, filePath)
            createCSV(filePath, T, matricesPathList)
        T = getTransMatrix(fullText, filePath)
        createCSV(filePath, T, matricesPathList, True)

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

# File path here is used to locate the folder directory and create
# abbrivation for books
def createCSV(filePath, T, matricesPathList, isComposite = False):
    filePath = filePath.split("/")
    outputPath = "./%s/%s" % (filePath[1]+" Matrices", filePath[1].replace(" ", ""))
    if isComposite:
        outputPath += "Composite"
    else:
        bookName = filePath[2].split(" ")
        for word in bookName:
            outputPath += word[0].upper()
    outputPath += ".csv"
    print("saving matrix result to", outputPath)
    df = pd.DataFrame(data=T, columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "space", "symbol"])
    df.to_csv(outputPath, index=False, encoding='utf8')
    matricesPathList.write(outputPath + "\n")

if __name__ == '__main__':
    main()
