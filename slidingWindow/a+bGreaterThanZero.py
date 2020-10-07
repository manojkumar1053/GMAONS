def smallest_subarray_with_given_sum(s, arr):
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
