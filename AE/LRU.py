class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1

    def insertKeyValuePair(self, key, value):
        # Write your code here.
        pass

    def getValueFromKey(self, key):
        # Write your code here.
        pass

    def getMostRecentKey(self):
        # Write your code here.
        pass


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHeadTo(self,node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev =node
            self.head = node
            self.head.next = self.tail


class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def removeBindings(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.next = None
        self.prev = None
