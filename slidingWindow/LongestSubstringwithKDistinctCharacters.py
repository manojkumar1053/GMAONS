def longest_substring_with_k_distinct(str1, k):
    windowStart = 0
    maxLength = 0
    charFrequency = {}
    # create a frequency table of all chars
    for windowEnd in range(len(str1)):
        if str1[windowEnd] not in charFrequency:
            charFrequency[str1[windowEnd]] = 1
        else:
            charFrequency[str1[windowEnd]] += 1
        # # shrink the sliding window, until we are left with 'k' distinct characters
        while len(charFrequency) > k:
            charFrequency[str1[windowStart]] -= 1
            if charFrequency[str1[windowStart]] == 0:
                del charFrequency[str1[windowStart]]
            windowStart += 1
        maxLength = max(maxLength, windowEnd - windowStart + 1)
    return maxLength


def main():
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
