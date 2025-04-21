class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev # 왼쪽에 있는 노드 주소
        self.next = next # 오른쪽에 있는 노드 주소

class DListType: # 헤드 노드 사용
    def __init__(self):
        self.head = Node(0) # 헤드 포인터가 아니라 헤드 노드를 만들어야 함
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def insert(self, pos, data):
        if pos <= 0 or pos > self.size + 1:
            print("Invalid Pos.")
            return

        p = self.head # 이 부분이 다름: 헤드 노드이기 때문에 헤드를 가리킬 수 있게 됨
        for _ in range(1, pos): # pos-1번 노드에서 멈춤
            p = p.next

        node = Node(data)
        node.prev = p # 누굴 가리키지?
        node.next = p.next # 누굴 가리키지?
        p.next.prev = node # 누가 날 가리키지?(순서 중요)
        p.next = node # 누가 날 가리키지?(순서 중요)

        self.size += 1

    def delete(self, pos):
        if pos <= 0 or pos > self.size :
            print("Invalid Pos.")
            return

        p = self.head
        for _ in range(0, pos): # pos번 노드에서 멈춤
            p = p.next

        data = p.data
        p.prev.next = p.next
        p.next.prev = p.prev

        self.size -=1

        return data


    def printList(self):
        p = self.head.next

        while p != self.tail: # tail 노드를 찍으면 안 되므로
            print("[%s] <=> " % p.data, end="")
            p = p.next
        print('\b\b\b\b       ')

if __name__ == '__main__':
    DL = DListType()

    DL.insert(1, 'A'); DL.printList()
    DL.insert(1, 'B'); DL.printList()
    DL.insert(2, 'C'); DL.printList()
    DL.insert(4, 'D'); DL.printList()

    print('[%s] is deleted.' % DL.delete(1)); DL.printList()







