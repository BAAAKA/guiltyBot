import os
from author import author
#text_file = open("token.txt", "r")
#token = text_file.readlines()[0]


txtFilePath = os.getcwd() + "\\authors"
print(txtFilePath)



def getFiles(path):
    filePaths = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(txtFilePath, file)) and file.endswith(".txt"):
            print(file)
            print("--")
            filePaths.append(file)

    return filePaths

def createAuthros(txtFilePath):
    authors = {}
    filePaths = getFiles(txtFilePath)
    for file in filePaths:
        authorName = str(file.replace('.txt', ''))
        print(type(file))
        names = ["a Name", "a second name"]
        quotes =["a Text", "a second quote"]
        authors[authorName] = author(names, quotes)
    return authors

authors = createAuthros(txtFilePath)

print(authors)

for author in authors:
    print("type")
    print(type(author))
    for name in author.names:
        print(name)
    for quote in author.quotes:
        print(quote)