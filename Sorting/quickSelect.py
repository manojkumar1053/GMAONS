def quickSelect(array, k):
    return quickSelectHelper(array, 0, len(array) - 1, k - 1)


def quickSelectHelper(array, startIdx, endIdx, position):
    while True:
        if startIdx > endIdx:
            raise Exception("Error !!!")
        pivotIndex = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx
        while leftIdx <= rightIdx:
            if array[leftIdx] > array[pivotIndex] and array[rightIdx] < array[pivotIndex]:
                swap(array, leftIdx, rightIdx)
            if array[leftIdx] < array[pivotIndex]:
                leftIdx += 1
            if array[rightIdx] > array[pivotIndex]:
                rightIdx -= 1
        swap(array, pivotIndex, rightIdx)
        if rightIdx == position:
            return array[rightIdx]
        elif array[rightIdx] < position:
            startIdx = rightIdx + 1
        else:
            endIdx = rightIdx - 1


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
