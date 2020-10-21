def heapSort(array):
    # Write your code here.
    buildMaxHeap(array)
    for endIdx in reversed(range(1, len(array))):
        swap(0, endIdx, array)
        siftDown(0, endIdx - 1, array)
    return array


def buildMaxHeap(array):
    firstParentIdx = (len(array) - 1) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currentIdx, len(array) - 1, array)


def siftDown(currentIdx, endIdx, heap):
    childOneIdx = currentIdx * 2 + 1
    while childOneIdx <= endIdx:
        childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
        if childTwoIdx >= -1 and heap[childTwoIdx] > heap[childOneIdx]:
            idxSwap = childTwoIdx
        else:
            idxSwap = childOneIdx
        if heap[idxSwap] > heap[currentIdx]:
            swap(currentIdx, idxSwap, heap)
            currentIdx = idxSwap
            childOneIdx = currentIdx * 2 + 1
        else:
            return


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
