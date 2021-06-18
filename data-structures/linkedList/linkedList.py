class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)


class SNode:
    def __init__(self, data):
        if data is None:
            raise ValueError("Node data cannot be None")
        if type(data) not in [int, str]:
            raise TypeError("Only integer and string datatypes are permitted.")
        self.data = data
        self.next = None
        

class SLinkedList:
    def __init__(self, head = None):
        if head is not None:
            if type(head) is not SNode:
                raise TypeError("Head must be Node.")
        self.head = head

    def addNodeAtStart(self, data):
        newNode = SNode(data)
        newNode.next = self.head
        self.head = newNode

    def addNodeAtEnd(self, data):
        newNode = SNode(data)
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            previousNode = self.head
            while currentNode is not None:
                previousNode = currentNode
                currentNode = currentNode.next
            previousNode.next = newNode

    def getSequence(self):
        sequence = ""
        currentNode = self.head
        while currentNode is not None:
            sequence += currentNode.data
            currentNode = currentNode.next
            if currentNode is not None:
                sequence += "->"
        return sequence








class DNode:
    def __init__(self, data):
        if data is None:
            raise ValueError("Node data cannot be None")
        if type(data) not in [int, str]:
            raise TypeError("Only integer and string datatypes are permitted.")
        self.data = data
        self.previous = None
        self.next = None


class DLinkedList:
    def __init__(self):
        pass

