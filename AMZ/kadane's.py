def kadanesAlgorithm(array):
    # Write your code here.
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for num in array[1:]:
        maxEndingHere = max(maxEndingHere + num, num)
        # if maxEndingHere+num < num:
        #     print("index",array.index(num))
        maxSoFar = max(maxSoFar, maxEndingHere)
        # if maxEndingHere > maxSoFar:
        #     print("indexE",array.index(num))

    return maxSoFar


print("maxSubArraysSum", kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
