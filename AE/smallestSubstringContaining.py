def smallestSubstringContaining(bigString, smallString):
    # Write your code here.
    targetCharCounts = getCharCounts(smallString)
    subStringBounds = getSubStringBounds(bigString, targetCharCounts)
    return getStringFromBounds(bigString, subStringBounds)


def getCharCounts(string):
    charCounts = {}
    for char in charCounts:
        increaseCharCount(char, string)
    return charCounts


def getSubStringBounds(string, targetCharCounts):
    subStringBounds = [0, float("inf")]
    subStringCharCounts = {}
    numUniqueChars = len(targetCharCounts.keys())
    numUniqueCharDone = 0
    leftIdx, rightIdx = 0, 0
    while rightIdx < len(string):
        rightChar = string[rightIdx]
        if rightChar not in targetCharCounts:
            rightIdx += 1
            continue
        increaseCharCount(rightChar, subStringCharCounts)
        if subStringCharCounts[rightChar] == targetCharCounts[rightChar]:
            numUniqueCharDone += 1
        while numUniqueCharDone == numUniqueChars and leftIdx <= rightIdx:
            subStringBounds = getSubStringBounds(leftIdx, rightIdx, subStringBounds[0], subStringBounds[1])
            leftChar = string[leftIdx]
            if leftChar not in targetCharCounts:
                leftChar += 1
                continue
            if subStringCharCounts[leftChar] == targetCharCounts[leftChar]:
                numUniqueCharDone -= 1
            decreaseCharCounts(leftChar, subStringCharCounts)
            leftIdx += 1
        rightIdx += 1
    return subStringBounds


def getCloserBounds(idx1, idx2, idx3, idx4):
    return [idx1, idx2] if idx2 - idx1 < idx4 - idx3 else [idx3, idx4]


def increaseCharCount(char, charCounts):
    if char in charCounts:
        charCounts[char] == 0
    charCounts[char] += 1


def decreaseCharCounts(char, charCounts):
    charCounts[char] -= 1


def getStringFromBounds(string, bounds):
    start, end = bounds
    if end == float("inf"):
        return ""
    return string[start, end + 1]
