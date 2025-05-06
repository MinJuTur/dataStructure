class ArrayQueue: #선형큐 -> 실제 사용하지 않음
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.array = [None] * capacity # 아무것도 없음을 전체에 채워넣기

    def isEmpty(self): # 계속 오른쪽으로 움직이기 때문에 -1인지 비교하면 안 됨
        return self.front == self.rear # front: 원소 자체를 가리키지 않음, rear: 원소 자체를 가리킴

    def isFull(self):
        return self.rear == self.capacity - 1

    def enqueue(self, e):
        if not self.isFull():
            self.rear += 1
            self.array[self.rear] = e
        else:
            print('Overflow')

    def dequeue(self):
        if not self.isEmpty():
            self.front += 1
            return self.array[self.front]
        else:
            print('Underflow')

    def display(self):
        print('Front : %d, Rear : %d' % (self.front, self.rear))
        print(self.array[self.front+1:self.rear+1])

if __name__ == '__main__':
    Q = ArrayQueue(10)

    data = ['A', 'B','C', 'D', 'E']

    for e in data:
        Q.enqueue(e)
    Q.display()

    print('Dequeue => ', Q.dequeue())
    print('Dequeue => ', Q.dequeue())
    Q.display()

    for e in data:
        Q.enqueue(e)
    Q.display()

    print('Dequeue => ', Q.dequeue())
    print('Dequeue => ', Q.dequeue())
    Q.display()

    Q.enqueue('F') # Overflow 발생 <- 4칸이 비어있음에도 불구하고 (선형큐의 문제)
    Q.display()