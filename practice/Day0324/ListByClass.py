class ArrayList:

    def __init__(self, capacity=100):
        self.capacity = 100
        self.size = 0
        self.array = [None] * capacity

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size: # pos는 size까지 포함돼야 함
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1
        else:
            print("Overflow or Invalid Position.")

    def delete(self, pos):
        global size
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos,self.size-1):
                self.array[i] = self.array[i+1]
            self.size -= 1
            return e
        else:
            print("Underflow or Invalid Position.")

    def getEntry(self, pos):
        if (0 <= pos < self.size):
            return self.array[pos]
        else:
            return None

    def __str__(self):
        return str(self.array[0:self.size])

if __name__ == '__main__':
    L = ArrayList(50)
    L.insert(0, 'A')
    L.insert(1, 'B')
    L.insert(1, 'C')
    print(L)

    L.insert(4, 'D')
    L.insert(3, 'E')
    print(L)

    print('Deleted : %c' % L.delete(1))
    print(L)