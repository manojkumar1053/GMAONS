def smallestSubstringContaining(bigString, smallString):
    # Write your code here.
    targetCharCounts = getCharCounts(smallString)


def getCharCounts(string):
    charCounts = {}
    for char in string:
        increaseCharCount(char, charCounts)

def getSubStringBounds(string, targetCharCounts):
    pass


def increaseCharCount(char, charCounts):
    if char not in charCounts:
        charCounts[char] = 0
    charCounts[char] += 1


def decreaseCharCounts(char, charCounts):
    charCounts[char] -= 1
