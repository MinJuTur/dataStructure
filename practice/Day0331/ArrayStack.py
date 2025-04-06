class ArrayStack:
    def __init__(self, capacity = 20):
        self.capacity = capacity
        self.top = -1 # 상단의 요소를 가리킴
        self.array = [None] * capacity # 아무것도 없음을 전체에 채워넣기

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else:
            print('Overflow.')

    def pop(self):
        if not self.isEmpty():
            e = self.array[self.top]
            self.top -= 1
            return e
        else:
            print('Underflow.')

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            print('Underflow.')

    def display(self):
        print()
        for i in range(self.top, -1, -1):
            print(' | %d |' % (self.array[i]))
            print(' -----')
        print()

if __name__ == '__main__':
    S = ArrayStack()

    data = [5,3,8,1,2,7]

    for e in data:
        S.push(e)
    S.display()

    print('Popped [%d]' % S.pop())
    S.display()

    print('Peeked [%d]' % S.peek())
    S.display()