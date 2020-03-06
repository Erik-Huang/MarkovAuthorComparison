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
            '''
            T = getTransMatrix(text, filePath)
            createCSV(filePath, T, matricesPathList)
            '''
            T_b = getNgramTransMatrix(text, filePath, 2)
            createBigramCSV(filePath, T_b, matricesPathList)
            '''
            T_t = getNgramTransMatrix(text, filePath, 3)
            createTrigramCSV(filePath, T_t, matricesPathList)
            '''
        T = getTransMatrix(fullText, filePath)
        createCSV(filePath, T, matricesPathList, True)
        T_b = getNgramTransMatrix(fullText, filePath, 2)
        createBigramCSV(filePath, T_b, matricesPathList, True)
        #T_t = getNgramTransMatrix(fullText, filePath, 3)
        #createTrigramCSV(filePath, T_t, matricesPathList, True)

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
    return T

def getNgramTransMatrix(text, filePath, n):
	T = [[0 for c in range(COLS ** n)] for r in range(ROWS ** n)]
	for i in range(1, len(text) - n):
		nextKey = [text[i]]
		prevKey = [text[i - 1]]
		for j in range(1, n):
			nextKey += text[i + j]
			prevKey += text[i + j - 1]
		next = getNgramIndex(nextKey)
		prev = getNgramIndex(prevKey)
		T[prev][next] += 1
	for row in range(len(T)):
		rowSum = sum(T[row])
		if rowSum != 0:
			for col in range(len(T[row])):
				T[row][col] = T[row][col] / rowSum
		else:
			#print("warning: zero sum row in", filePath)
			for col in range(len(T[row])):
				T[row][col] = 1 / len(T[row])
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

def getNgramIndex(carr):
	ind = 0;
	for i in range(len(carr)):
		ind = ind + getIndex(carr[i]) * (ROWS ** (len(carr) - (i + 1)))
	return ind

def reverseName(author):
    author = author.split(", ")
    return author[1]+" "+author[0]

def createCSV(filePath, T, matricesPathList, isComposite = False):
    filePath = filePath.split("/")
    outputPath = "./%s/%s" % (filePath[1]+" Matrices", filePath[1].replace(" ", ""))
    if isComposite:
        outputPath += "Composite"
    else:
        bookName = filePath[2].split(" ")
        for word in bookName:
            outputPath += word[0].upper()
    outputPath += "1"
    outputPath += ".csv"
    print("saving matrix result of", filePath[2])
    df = pd.DataFrame(data=T, columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "space", "symbol"])
    df.to_csv(outputPath, index=False, encoding='utf8')
    matricesPathList.write(outputPath + "\n")

def createBigramCSV(filePath, T, matricesPathList, isComposite = False):
	filePath = filePath.split("/")
	outputPath = "./%s/%s" % (filePath[1]+" Matrices", filePath[1].replace(" ", ""))
	bookName = filePath[2].split(" ")
	if isComposite:
		outputPath += "Composite"
	else:
		bookName = filePath[2].split(" ")
		for word in bookName:
			outputPath += word[0].upper()
	outputPath += "2"
	outputPath += ".csv"
	print("saving matrix result of", filePath[2])
	keys2 = createBigramLabels()
	df = pd.DataFrame(data=T, columns=keys2)
	df.to_csv(outputPath, index=False, encoding='utf8')
	matricesPathList.write(outputPath + "\n")

def createTrigramCSV(filePath, T, matricesPathList, isComposite = False):
	filePath = filePath.split("/")
	outputPath = "./%s/%s" % (filePath[1]+" Matrices", filePath[1].replace(" ", ""))
	bookName = filePath[2].split(" ")
	if isComposite:
		outputPath += "Composite"
	else:
		bookName = filePath[2].split(" ")
		for word in bookName:
			outputPath += word[0].upper()
	outputPath += "3"
	outputPath += ".csv"
	print("saving matrix result of", filePath[2])
	keys2 = createTrigramLabels()
	df = pd.DataFrame(data=T, columns=keys2)
	df.to_csv(outputPath, index=False, encoding='utf8')
	matricesPathList.write(outputPath + "\n")

def createBigramLabels():
	labs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "space", "symbol"];
	labs_out = []
	for c1 in labs:
		for c2 in labs:
			labs_out.append(c1 + c2)
	return labs_out

def createTrigramLabels():
	labs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "space", "symbol"];
	labs_out = []
	for c1 in labs:
		for c2 in labs:
			for c3 in labs:
				labs_out.append(c1 + c2 + c3)
	return labs_out

if __name__ == '__main__':
    main()
