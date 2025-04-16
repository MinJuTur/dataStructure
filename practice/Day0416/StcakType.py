class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class StackType:
    def __init__(self):
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push(self, data):
        node = Node(data)
        node.next = self.top

        self.top = node
        self.size += 1

    def pop(self):
        if not self.isEmpty():
            p = self.top
            self.top = p.next
            self.size -= 1
            return p.data
        else:
            print('Underflow')

    def printList(self):
        p = self.top

        while p != None:
            print('[%s] -> ' % (p.data), end='')
            p = p.next
        print('\b\b\b    ')