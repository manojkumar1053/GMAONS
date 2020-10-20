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


def binarySearch1(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper1(array, target, left, right):
    while left < right:
        middle = (left + right) // 2
        targetMatch = array[middle]
        if target == targetMatch:
            return middle
        elif target < targetMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1
