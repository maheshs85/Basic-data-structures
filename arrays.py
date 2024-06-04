class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def insert(self, index, value):
        if self.is_full():
            raise Exception("Array is full")
        if index < 0 or index > self.size:
            raise Exception("Index out of bounds")
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.size += 1

    def append(self, value):
        if self.is_full():
            raise Exception("Array is full")
        self.data[self.size] = value
        self.size += 1

    def delete(self, index):
        if self.is_empty():
            raise Exception("Array is empty")
        if index < 0 or index >= self.size:
            raise Exception("Index out of bounds")
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size -= 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise Exception("Index out of bounds")
        return self.data[index]

    def display(self):
        return [self.data[i] for i in range(self.size)]
