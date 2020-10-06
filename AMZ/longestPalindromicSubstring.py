def longestPalindromicSubstring(string):
    currentLogestString = [0, 1]
    for i in range(1, len(string)):
        odd = getLPFrom(string, i - 1, i + 1)
        even = getLPFrom(string, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLogestString = max(longest, currentLogestString, key=lambda x: x[1] - x[0])
    return string[currentLogestString[0]:currentLogestString[1]]


def getLPFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx <= len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1  # breaks after   -1
        rightIdx += 1  # breaks after  + 1
    return [leftIdx + 1, rightIdx]
