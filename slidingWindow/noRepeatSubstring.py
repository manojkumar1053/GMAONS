def non_repeat_substring(str1):
    windowStart = 0
    maxLength = 0
    charFrequency = {}

    for windowEnd in range(len(str1)):
        if str1[windowEnd] in charFrequency:
            windowStart = max(windowStart, charFrequency[str1[windowEnd]] + 1)
        charFrequency[str1[windowEnd]] = windowEnd
        maxLength = max(maxLength, windowEnd - windowStart + 1)
    return maxLength


def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()
