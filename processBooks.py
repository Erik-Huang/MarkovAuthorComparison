import re
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

ID_TAG = "rdf:ID="
TITLE_TAG = "dc:title"
DOWNLOAD_URL = "http://www.gutenberg.org/cache/epub/"
START_TAG = "START OF"
END_TAG = "END OF"

def main():
    for author in AUTHOR_LIST:
        #findBookForAuthor(author)
        downloadBooksForAuthor(author)
        #pruneBookInput(author)

def findBookForAuthor(author):
    fileInput = open("catalog.rdf", "r")
    lines = fileInput.readlines()
    bookDict = {}
    count = 0
    for i in range(len(lines)):
        if author in lines[i]:
            count += 1
            nextIndex = i - 1
            id = -1
            name = ""
            for k in range(15):
                nextLine = lines[nextIndex]
                if ID_TAG in nextLine:
                    id = nextLine[28:-3]
                if TITLE_TAG in nextLine:
                    name = nextLine.split(">")[1][:-10]
                nextIndex -= 1
            if id != -1 and name != "":
                bookDict[id] = name
            else:
                print("not found at index", i)
    for id in bookDict:
        print("%6s   %s" % (id, bookDict[id]))
    print(len(bookDict), "books found for ", author)
    fileInput.close()
    outputBookListForAuthor(author, bookDict)

def outputBookListForAuthor(author, bookDict):
    fileOutput = open("./bookList/"+author+".txt", "w+")
    for id in bookDict:
        fileOutput.write("%s|%s\n" % (id, bookDict[id]))
    fileOutput.close()

def downloadBooksForAuthor(author):
    fileInput = open("./bookList/"+author+".txt", "r")
    author = author.replace(" ", "\ ").split(",\ ")
    location =  "./%s\ %s/" % (author[1], author[0])
    os.system("mkdir " + location)
    for line in fileInput.readlines():
        sep = line.index("|")
        id = line[:sep]
        bookname = line[sep+1:-1].replace(" ", "\ ") + ".txt"
        cmd = "wget -O %s %s%s/pg%s.txt" % (location + bookname, DOWNLOAD_URL, id, id)
        os.system(cmd)

def pruneBookInput(author):
    filelist = []
    author = author.split(", ")
    location = "./%s %s/" % (author[1], author[0])
    for i in os.scandir(location):
        if i.is_file() and i.path.endswith(".txt"):
            filelist.append(i.path)
    for bookPath in filelist:
        fRead = open(bookPath, "r")
        temp = fRead.readlines();
        start_index = -1;
        end_index = -1;
        for i in range(len(temp)):
            if START_TAG in temp[i]:
                start_index = i
                break
        for i in range(len(temp)):
            if END_TAG in temp[len(temp)-i-1]:
                end_index = i
                break
        fRead.close()
        if (start_index == -1 or end_index == -1):
            print("No Pruning for", bookPath)
            continue
        else:
            temp = temp[start_index+1:end_index]
            fWrite= open(bookPath, "w+")
            for line in temp:
                fWrite.write(line)
            fWrite.close()
            print("Finished", bookPath)

if __name__ == '__main__':
    main()
