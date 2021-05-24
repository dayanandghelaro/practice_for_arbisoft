class ValidationError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)

        self.errors = errors
        
class Stack:
    def __init__(self, size, dataType=int):
        if type(size) is not int:
            raise TypeError("Size of stack can only be integer.")
        if size <= 0:
            raise ValueError("Size of stack must be positive integer.")
        self.size = size
        self.dataType = dataType
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.size

    def push(self, itemValue):
        if type(itemValue) is not self.dataType:
            raise TypeError("Datatype of item doesn't match with stack's items.")
        if self.isFull():
            raise ValidationError("Stack is full!", IndexError)
        self.stack.append(itemValue)

    def peek(self):
        if self.isEmpty():
            raise ValidationError("Stack is empty!", IndexError)
        return self.stack[-1]

    def pop(self):
        if self.isEmpty():
            raise ValidationError("Stack is empty!", IndexError)
        return self.stack.pop()
    
        
        

    
