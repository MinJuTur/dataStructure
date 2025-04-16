class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next # 오른쪽에 있는 노드 주소

class CircularList: # 노드들로 만들어지는 리스트
    def __init__(self):
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def insertLast(self, data):
        node = Node(data)

        if self.isEmpty(): # 아무것도 없을 때 insertLast()를 하면 첫 번째이자 마지막 node가 됨
            node.next = node # 누굴 가리키지? 내 자신을 가리키게 됨
            self.tail = node # 누가 날 가리키지?
        else:
            node.next = self.tail.next # 누굴 가리키지? 기존 마지막 node가 가리키고 있는 node
            self.tail.next = node # 누가 날 가리키지?
            self.tail = node

        self.size += 1


    def insertFirst(self, data):
        node = Node(data)

        if self.isEmpty(): # 아무것도 없을 때 insertFirst()를 하면 첫 번째이자 마지막 node가 됨
            node.next = node # 누굴 가리키지? 내 자신을 가리키게 됨
            self.tail = node # 누가 날 가리키지?
        else:
            # insertLast()의 코드와 self.tail = node 제외하고 동일(원형 리스트미으로)
            node.next = self.tail.next # 누굴 가리키지? 기존 마지막 node가 가리키고 있는 node
            self.tail.next = node # 누가 날 가리키지?

        self.size += 1

    def deleteFirst(self):
        # 화살표 두 개 필요
        if not self.isEmpty():
           p = self.tail # 마지막 node
           q = p.next # 첫 번째 node -> 삭제 예정
           if p == q: # node가 단 한 개만 존재할 때 <- 구분하지 않으면 그 다음 삽입이 불가
               self.tail = None
           else:
               p.next = q.next

           self.size -= 1
           return q.data # 삭제된 node 값 반환
        else:
            print('Underflow')


    def deleteLast(self):
        # 화살표 두 개 필요
        if not self.isEmpty():
            p = self.tail # 마지막 node -> 삭제 예정
            q = p.next # 첫 번째 node

            if p == q: # node가 단 한 개만 존재할 때 <- 구분하지 않으면 그 다음 삽입이 불가
                self.tail = None
            else:
                while q.next != p: # 마지막 node 전의 node가 될 때까지 반복
                    q = q.next
                q.next = p.next
                self.tail = q

            self.size -= 1
            return p.data # 삭제된 node 값 반환
        else:
            print('Underflow')


    def printList(self): # 원형 연결 리스트에서 가장 어려운 함수
        p = self.tail

        if not self.isEmpty():
            # do-while 문 대신(마지막 node 체크를 위해)
            while True:
                print('[%s] -> ' % (p.next.data), end='') # 출력한 다음에
                p = p.next  # 방금 출력한 node로 이동해야 함

                if p == self.tail:
                    break
            print('\b\b\b    ')



if __name__=='__main__':
    L = CircularList()

    L.insertLast('C'); L.printList()
    L.insertFirst('A'); L.printList()
    L.insertFirst('B'); L.printList()
    L.insertLast('D'); L.printList()

    print('[%c] is deleted.' % L.deleteFirst()); L.printList()
    print('[%c] is deleted.' % L.deleteLast()); L.printList()
