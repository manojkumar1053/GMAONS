def find_averages_of_subarrays(K, arr):
    result = []
    windowStart = 0
    windowSum = 0.0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if windowEnd >= K - 1:
            result.append(windowSum / K)
            windowSum -= arr[windowStart]
            windowStart += 1
    return result


def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()




