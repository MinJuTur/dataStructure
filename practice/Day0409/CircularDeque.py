from practice.Day0407.CircularQueue import CircularQueue

class CircularDeque(CircularQueue): # CircularQueue 기능 확장 -> CircularQueue 상속 받기

    def __init__(self, capacity = 10):
        super().__init__(capacity)

    def addRear(self, e): # enqueue 함수와 연결
        self.enqueue(e)

    def deleteFront(self): # dequeue 함수와 연결
        self.dequeue()

    def getFront(self): # peek 함수와 연결
        self.peek()

    def addFront(self, e):
        if not self.isFull():
            self.array[self.front] = e;
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            print('Overflow.')

    def deleteRear(self):
        if not self.isEmpty():
            e = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return e
        else:
            print('Underflow.')

    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else:
            print('Underflow.')

if __name__ == '__main__':

    import random

    DQ = CircularDeque()

    data = ['A', 'B','C', 'D']

    for i in range(4):
        DQ.addFront(random.randint(65, 90)) # 아스키 코드 A~Z(display 함수에서 문자열로 출력하므로)
    DQ.display()

    for i in range(4):
        DQ.addRear(random.randint(65, 90))
    DQ.display()

    for i in range(3):
        DQ.deleteRear()
    DQ.display()

    for i in range(3):
        DQ.deleteFront()
    DQ.display()





