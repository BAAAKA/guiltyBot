import random


class author:
    def __init__(self, names, quotes):
        self.names = names
        self.quotes = quotes

    def hasName(self, text):
        for name in self.names:
            if name.lower() in text.lower():
                return True
        return False

    def isName(self, text):
        for name in self.names:
            if name.lower() == text.lower():
                return True
        return False

    def ranQuote(self):
        x = random.randint(0, len(self.quotes) - 1)
        return self.quotes[x]

    def ranName(self):
        x = random.randint(0, len(self.names) - 1)
        return self.names[x]

    def getNames(self):
        return self.names

    def getQuotes(self):
        return self.quotes


GabeNames = ["gabe"]
GabeText = []
GabeText.append("Yes, front liner, every single character")
GabeText.append("Really? Martials, every single character?")

gabe = author(GabeNames, GabeText)
