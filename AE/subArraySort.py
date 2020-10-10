def subarraySort(array):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")
    for i in range (len(array)):
        num = array[i]

