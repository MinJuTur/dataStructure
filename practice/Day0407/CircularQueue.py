class CircularQueue: #원형큐
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = [None] * capacity # 아무것도 없음을 전체에 채워넣기

    def isEmpty(self): # 계속 오른쪽으로 움직이기 때문에 -1인지 비교하면 안 됨
        return self.front == self.rear # front: 원소 자체를 가리키지 않음, rear: 원소 자체를 가리킴

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity # rear 앞이 비어있는가

    def enqueue(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = e
        else:
            print('Overflow')

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            print('Underflow')

    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else:
            print('Underflow')

    def display(self): # 가장 까다로운 함수
        print('Front : %d, Rear : %d' % (self.front, self.rear))
        i = self.front

        while i != self.rear:
            i = (i + 1) % self.capacity
            print('[%c] ' % self.array[i], end='')
        print()



if __name__ == '__main__':
    Q = CircularQueue()

    data = ['A', 'B','C', 'D']

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

    Q.enqueue('F') # Overflow 발생하지 않음
    Q.display()