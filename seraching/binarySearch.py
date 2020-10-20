def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    matchTarget = array[middle]
    if target == matchTarget:
        return middle
    elif target < matchTarget:
        return binarySearchHelper(array, target, left, middle - 1)
    else:
        return binarySearchHelper(array, target, middle + 1, right)
