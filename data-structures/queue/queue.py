class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Queue:
    def __init__(self, size, dataType=int):
        if type(size) is not int:
            raise TypeError("Size can only be integer.")
        if size <= 0:
            raise ValueError("Size must be positive integer.")
        self.size = size
        self.dataType = dataType
        self.queue = []

    def isFull(self):
        return len(self.queue) == self.size

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, itemValue):
        if self.isFull():
            raise ValidationError("Queue is full!")
        if type(itemValue) is not self.dataType:
            raise TypeError("Datatype of item is different from queue's datatype.")
        self.queue.insert(0, itemValue)


    def dequeue(self):
        if self.isEmpty():
            raise ValidationError("Queue is empty!")
        return self.queue.pop()

    

    


