class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        pass

    def siftDown(self, currentIndex, endIdx, heap):
        # Write your code here.
        childOneIdx = currentIndex * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIndex * 2 + 2 if currentIndex * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] <= heap[childOneIdx]:
                idxSwap = childTwoIdx
            else:
                idxSwap = childOneIdx
            if heap[idxSwap] < heap[currentIndex]:
                self.swap(currentIndex, idxSwap, self.heap)
                currentIndex = idxSwap
                childOneIdx = currentIndex * 2 + 1
            else:
                break

    def siftUp(self, currentIndex, heap):
        parentIdx = (currentIndex - 1) // 2
        while currentIndex > 0 and heap[currentIndex] < heap[parentIdx]:
            self.swap(currentIndex, parentIdx, heap)
            currentIndex = parentIdx
            parentIdx = (currentIndex - 1) // 2

    def peek(self):
        # Write your code here.
        pass

    def remove(self):
        # Write your code here.
        self.swap(0, len(self.heap), self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
