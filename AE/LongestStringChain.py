def longestStringChain(strings):
    # Write your code here.
    stringChains = {}
    for string in strings:
        stringChains[string] = {
            "nextString": "",
            "maxChainLength": 1
        }
    sortedString = sorted(strings, key=len)
    for string in sortedString:
        findLongestStringChain(string, stringChains)
        pass


def findLongestStringChain(string, stringChains):
    for i in range(len(string)):
        smallerString = getSmallerString(string, i)
        if smallerString not in stringChains:
            continue
        tryUpdateLongestStringChain(string, smallerString, stringChains)


def getSmallerString(string, index):
    return string[0:index] + string[index + 1:]


def tryUpdateLongestStringChain(currentString, smallerString, stringChains):
    smallerStringChainLength = stringChains[smallerString]["maxChainLength"]
    currentStringChainLength = stringChains[currentString]["maxChainLength"]

    if smallerStringChainLength +1 >=currentStringChainLength:
        stringChains[currentString]["maxChainLength"] = smallerStringChainLength+1
        stringChains[currentString]["nextString"] = smallerString


