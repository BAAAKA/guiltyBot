import os
from author import author

class logic:
    def __init__(self):
        print("[INFO] ##################################")
        print("[INFO] Beginn main.py")
        print("[INFO] ##################################")

        """
        for author in authors:
            print("type")
            print(type(author))
            for name in author.names:
                print(name)
            for quote in author.quotes:
                print(quote)
        """
        txtFilePath = os.getcwd() + "\\authors"
        print("[INFO] FILEPATH: {}".format(txtFilePath))

        print("[INFO] CREATING AUTHORS")
        self.authors = self.createAuthors(txtFilePath)



    def getQuote(self, message):
        print("[INFO][getQuote] got the message: {}".format(message))
        print("[INFO][getQuote] have the authors: {}".format(self.authors))

        for author in self.authors:
            if author.hasName(message):
                quote = author.ranQuote()
                print("[INFO][getQuote] in MESSAGE: {} found the name of {}; going to return quote: {}".format(message, author.ranName, quote))
                return quote
        return None


    def getFiles(self, txtFilePath):
        filePaths = []
        for file in os.listdir(txtFilePath):
            if os.path.isfile(os.path.join(txtFilePath, file)) and file.endswith(".txt"):
                print("[INFO][getFiles] Found txt file: {} in folder: {}".format(file, txtFilePath))
                filePaths.append(file)

        return filePaths

    def readFile(self, file, txtFilePath):
        filepath = txtFilePath + "\\" + file
        text_file = open(filepath, "r")
        lines = text_file.readlines()
        print("[INFO][readFile] FILEPATH: {} has the CONTENT: {}".format(filepath, lines))
        text_file.close()
        return lines

    def nameQuoteSort(self, fileContent):
        print("[INFO][nameQuoteSort] Going to nameQuoteSort content: {}".format(fileContent))
        names = []
        quotes = []
        for line in fileContent:
            line = line.strip()
            if "NAME:" in line:
                print("[INFO][nameQuoteSort] NAME: Match: \"{}\"".format(line))
                name = line.replace("NAME:", "")
                names.append(name)
            elif "QUOTE:" in line:
                print("[INFO][nameQuoteSort] QUOTE: Match: \"{}\"".format(line))
                quote = line.replace("QUOTE:", "")
                quotes.append(quote)
            else:
                print("[WARNING][nameQuoteSort] NO NAME: or QUOTE: match in line: {}, will be ignored".format(line))
        return names, quotes

    def createAuthors(self, txtFilePath):
        authors = []
        filePaths = self.getFiles(txtFilePath)
        for file in filePaths:
            fileContent = self.readFile(file, txtFilePath)
            names, quotes = self.nameQuoteSort(fileContent)
            authors.append(author(names, quotes))
        return authors



