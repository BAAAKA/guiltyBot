import random


class author:
    def __init__(self, names, quotes):
        self.names = names
        self.quotes = quotes

    def hasName(self, text):
        for name in self.names:
            if name in text:
                return True
        return False

    def ranQuote(self):
        x = random.randint(0, len(self.quotes) - 1)
        return self.quotes[x]


GabeNames = ["gabe"]
GabeText = []
GabeText.append("Yes, front liner, every single character")
GabeText.append("Really? Martials, every single character?")

gabe = author(GabeNames, GabeText)
