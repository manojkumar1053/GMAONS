"""
Given an array of positive numbers
and a positive number ‘S’,
find the length of the smallest
contiguous subarray whose sum is greater than or equal to ‘S’.
Return 0, if no such subarray exists
"""


def smallest_subarray_with_given_sum(s, arr):
    if len(arr) < 1:
        return 0
    windowMin = float("inf")
    windowSum = 0.0
    windowStart = 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        while windowSum >= s:
            windowMin = min(windowMin, windowEnd - windowStart + 1)
            windowSum -= arr[windowStart]
            windowStart += 1
    return 0 if windowMin == float("inf") else windowMin


def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
