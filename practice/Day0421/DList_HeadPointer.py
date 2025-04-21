class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev # 왼쪽에 있는 노드 주소
        self.next = next # 오른쪽에 있는 노드 주소

class DListType: # 헤드 포인터 사용
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def insertFirst(self, data): # 헤드 노드이기 때문에 insert 함수만으론 불가
        node = Node(data, next = self.head) # prev = None(헤드 노드이므로)

        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.head.prev = node
            self.head = node

        self.size += 1

    def insertLast(self, data):
        node = Node(data, prev = self.tail)

        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1


    def printList(self):
        p = self.head

        while p != None: # tail 노드를 찍으면 안 되므로
            print("[%s] <=> " % p.data, end="")
            p = p.next
        print('\b\b\b\b       ')

if __name__ == '__main__':
    DL = DListType()

    DL.insertLast('C'); DL.printList()
    DL.insertFirst('A'); DL.printList()
    DL.insertFirst('B'); DL.printList()
    DL.insertLast('D'); DL.printList()
