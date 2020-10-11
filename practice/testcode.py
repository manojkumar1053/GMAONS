# # # capacity = 10
# # # items = 4
# # #
# # # kpc = [[0 for x in range(0, capacity + 1)]]
# # # kit = [[0] for y in range(0, items + 1)]
# # # kittest = [0 for y in range(0, items + 1)]
# # # print(kittest)
# # #
# # # kp_total = [[0 for x in range(0, capacity + 1)] for y in range(0, items + 1)]
# # #
# # # print("kpc", kpc)
# # # print("kit", kit)
# # # print(kp_total)
# # # print(items[2][2])
# # #
# # #
# #
# # #
# # # def prime(n):
# # #     #primeNumber = []
# # #     sieve = [True] * n
# # #     for i in range(3, int(n ** 0.5) + 1, 2):
# # #         if sieve[i]:
# # #             sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
# # #     primeNumber = [2] + [i for i in range(3, n, 2) if sieve[i]]
# # #     return len(primeNumber)
# # #
# # #
# # # print(prime(10))
# #
# #
# # # string = "ONS"
# # #
# # # print([[False for i in range(len(string))]for j in range(len(string))])
# #
# # # words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
# # #
# # # # print([sorted(w) for w in words])
# # # sw1 = [sorted(w) for w in words]
# # #
# # # print(sw1)
# # #
# # # sw2 = ["".join(sorted(w)) for w in words]
# # # print(sw2)
# # #
# # # indices = [i for i in range(len(words))]
# # # print(indices)
# # #
# # # x = indices.sort(key=lambda x:sw2[x])
# # # print(x)
# # # print(indices)
# #
# # # def longest_substring_with_k_distinct(str1, k):
# # #     charFrequency = {}
# # #     winStart = 0
# # #     maxLength = 0
# # #
# # #     for windowEnd in str1:
# # #         if windowEnd not in charFrequency:
# # #             charFrequency[windowEnd] = 1
# # #         else:
# # #             charFrequency[windowEnd] += 1
# # #         # return len(charFrequency)
# # #         while len(charFrequency) > k:
# # #             leftChar = str1[winStart]
# # #             charFrequency[leftChar] -= 1
# # #             if charFrequency[leftChar] == 0:
# # #                 del charFrequency[leftChar]
# # #             winStart += 1
# # #             #print(windowEnd)
# # #             #wrong output
# # #         maxLength = max(maxLength, str1.index(windowEnd)-winStart + 1)
# # #     return maxLength
# # #
# # #
# # # def main():
# # #     print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 2)))
# # #     print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 1)))
# # #     print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("cbbebi", 3)))
# # #
# # #
# # # main()
# #
# #
# # def longest_substring_with_k_distinct(str1, k):
# #     charFrequency = {}
# #     windowStart = 0
# #     maxLength = 0
# #
# #     for windowEnd in range(len(str1)):
# #
# #         # Create a frequency Table
# #         if str1[windowEnd] not in charFrequency:
# #             charFrequency[str1[windowEnd]] = 1
# #         else:
# #             charFrequency[str1[windowEnd]] += 1
# #     # shrink the sliding window, until we are left with 'k'
# #         # distinct characters in the char_frequency
# #         while len(charFrequency) > k:
# #             charFrequency[str1[windowStart]] -= 1
# #             if charFrequency[str1[windowStart]] == 0:
# #                 del charFrequency[str1[windowStart]]
# #             windowStart += 1
# #         maxLength = max(maxLength, windowEnd - windowStart + 1)
# #     return maxLength
# #
# #
# # def main():
# #     print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 2)))
# #     print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 1)))
# #     print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("cbbebi", 3)))
# #
# #
# # main()
#
# # def oldestStudent(ages):
# #
# #   value = list(ages.values())
# #   key = list(ages.keys())
# #   return key[value.index(max(value))]
# #
# # ages = {
# #      "Peter": 10,
# #      "Isabel": 11,
# #      "Anna": 9,
# #      "Thomas": 10,
# #      "Bob": 10,
# #      "Joseph": 11,
# #      "Maria": 12,
# #      "Gabriel": 10,
# #   }
# # #print(oldestStudent(ages))
# #
# # ages = {
# #     "Peter": 10,
# #     "Isabel": 11,
# #     "Anna": 9,
# #     "Thomas": 10,
# #     "Bob": 10,
# #     "Joseph": 11,
# #     "Maria": 12,
# #     "Gabriel": 10,}
# # value = list(ages.values())
# # #rint("v",value.index(max(value)))
# # key = list(ages.keys())
# # x =key[value.index(max(value))]
#
# # print(value)
# # print(key[1])
#
# # max_value = list(ages.values())
# # array = value[:]
# # array.sort()
# # max = array[-1]
# # secondMax = 0
# # for i in reversed(range(len(array))):
# #     if array[i] < max:
# #         secondMax = array[i]
# #         break
# #
# # y = key[value.index(secondMax)]
# # print(x,y)
# #
# #
# # newlist = array.remove(array[-1])
# # print("nl",newlist)
#
# # def calculateAverageAge(students):
# #   add_age = 0
# #   for thing in students.values():
# #       age = thing['age']
# #       add_age = add_age + age
# #
# #   return(add_age / len(students.keys()))
# #
# # students = {
# #       "Peter": {"age": 10, "address": "Lisbon"},
# #       "Isabel": {"age": 11, "address": "Sesimbra"},
# #       "Anna": {"age": 9, "address": "Lisbon"},
# #       "Gibrael": {"age": 10, "address": "Sesimbra"},
# #       "Susan": {"age": 11, "address": "Lisbon"},
# #       "Charles": {"age": 9, "address": "Sesimbra"},
# #   }
# # print(calculateAverageAge(students))
#
#
# # students = {
# #       "Peter": {"age": 10, "address": "Lisbon"},
# #       "Isabel": {"age": 11, "address": "Sesimbra"},
# #       "Anna": {"age": 9, "address": "Lisbon"},
# #       "Gibrael": {"age": 10, "address": "Sesimbra"},
# #       "Susan": {"age": 11, "address": "Lisbon"},
# #       "Charles": {"age": 9, "address": "Sesimbra"},
# #   }
# #
# # age= []
# # for key1 in students.values():
# #     #print(list(key1.values())[0])
# #     #age.append(list(key1.values())[0])
# #     age.append(list(key1.values())[0])
# #
# #
# #
# # print(sum(age)/len(age))
#
#
# # def find_students(address, students):
# #   names = []
# #   for key, subdict in students.items():
# #        for sublist in subdict.values():
# #           if (sublist == address):
# #              names.append(key)
# #   return sorted(names)
# #
# # students = {
# #       "Peter": {"age": 10, "address": "Lisbon"},
# #       "Isabel": {"age": 11, "address": "Sesimbra"},
# #       "Anna": {"age": 9, "address": "Lisbon"},
# # }
# # print(find_students("Lisbon", students))
#
#
# # def fruits_into_baskets(fruits):
# #     charF = {}
# #     for char in fruits:
# #         if char not in charF:
# #             charF[char] = 1
# #         else:
# #             charF[char] += 1
# #     print(charF)
# #     # sorted output will be a Tuple  [('B', 3), ('C', 2), ('A', 1)]
# #     sortedCharF = sorted(charF.items(), key=lambda x: x[1], reverse=True)
# #     print(sortedCharF)
# #     numberOffruits = sortedCharF[0][1] + sortedCharF[1][1]
# #     return numberOffruits
# #
# #
# # def main():
# #     print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
# #     print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))
# #
# #
# # main()
#
#
# def non_repeat_substring(str1):
#     window_start = 0
#     max_length = 0
#     char_index_map = {}
#
#     # try to extend the range [windowStart, windowEnd]
#     for window_end in range(len(str1)):
#         right_char = str1[window_end]
#         # if the map already contains the 'right_char', shrink the window from the beginning so that
#         # we have only one occurrence of 'right_char'
#         if right_char in char_index_map:
#             # this is tricky; in the current window, we will not have any 'right_char' after its previous index
#             # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
#             window_start = max(window_start, char_index_map[right_char] + 1)
#             print("windowStart: ",window_start)
#         # insert the 'right_char' into the map
#         char_index_map[right_char] = window_end
#         # remember the maximum length so far
#         print("windowEnd: ",window_end)
#         max_length = max(max_length, window_end - window_start + 1)
#         print("maxLength: ",max_length)
#     return max_length
#
#
# def main():
#     print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
#     print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
#     print("Length of the longest substring: " + str(non_repeat_substring("abccde")))
#
#
# main()
# ctrl+Shift+A
def interweavingStrings(one, two, three):
    # Write your code here.
    if len(three) != len(one) + len(two):
        return False
    sx = one + two
    setxy = sorted(set(sx))
    setz = sorted(set(three))
    for char in setz:
        if char not in setxy:
            return False
    s1_sort = ["".join(sorted(w)) for w in one]
    s2_sort = ["".join(sorted(w)) for w in two]
    s3_sort = ["".join(sorted(w)) for w in three]

    s1_sort.sort()
    s2_sort.sort()
    s3_sort.sort()
    s4 = s1_sort + s2_sort

    for x in s3_sort:
        if x not in s4:
            return False
        else:
            return True


s1 = "sass"
s2 = "xyz"
s3 = "xsssyzm"
print(s1 + s2)
s1_sort = ["".join(sorted(w)) for w in s1]
s2_sort = ["".join(sorted(w)) for w in s2]
s3_sort = ["".join(sorted(w)) for w in s3]

s1_sort.sort()
s2_sort.sort()
s3_sort.sort()
s4 = s1_sort + s2_sort
# if s3_sort == s1_sort+s2_sort:
#     print("yes")
# else:
#     print("no")

for x in s3_sort:
    if x not in s4:
        print("No")
        break
    else:
        print("YES")
