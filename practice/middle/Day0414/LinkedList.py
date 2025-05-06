# 연결 리스트 == 헤드 포인터, 연결 리스트 안에 여러 개의 노드가 존재하는 것
# 우린 연결 리스트를 만드는 것, 연결 리스트를 만들기 위해서는 노드가 필요함 -> 연결 리스트와 노드는 별개의 개체
# 노드 클래스 만들기 -> 연결 리스트 만들기
# isFull 함수 필요 없음

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next # 오른쪽에 있는 노드 주소

class ListType: # 노드들로 만들어지는 리스트
    def __init__(self):
        self.head = None # 헤드 포인터 = None: 선생님은 있는데 그 앞에 학생이 아무도 없다는 뜻, 즉 비어 있는 리스트
        self.size = 0 # 학생 수

    def isEmpty(self):
        # return self.head == None
        return self.size == 0

    def insertFirst(self, data): # self: 리스트, data: 학생 이름
        # node = Node(data, self.head) 로 써도 가능
        node = Node(data) # node: 학생
        node.next = self.head # 누굴 가리키지?, self.head: 선생님이 잡고 있는 학생

        self.head = node # 누가 날 가리키지?
        self.size += 1

    def getNode(self, pos): # (pos - 1)번째 노드를 리턴하는 함수
        p = self.head
        for _ in range(1, pos-1): # 주어진 pos에 따라 몇 번 움직여야 하는지
            p = p.next
        return p

    def insert(self, pos, data):
            if pos == 1:
                self.insertFirst(data)
            else:
                if pos <= self.size + 1:
                    p = self.getNode(pos)

                    node = Node(data, p.next)
                    p.next = node
                    self.size += 1
                else:
                    print('Invalid Position')

    def deleteFirst(self):
        if not self.isEmpty():
            p = self.head # p가 없어질 예정
            self.head = p.next
            self.size -= 1
            return p.data
        else:
            print('Underflow')

    def delete(self, pos):
        # 화살표 p, q 필요: 삭제 전, 삭제할 대상 가리키기
        if pos <= 0 or pos > self.size:
            print("Invalid Pos.")
            return

        if not self.isEmpty():
            if pos == 1:
                return self.deleteFirst()  # deletedFirst()에서 반환 받은 p.data를 받아 다시 반환
            else:
                q = self.getNode(pos) # 삭제할 노드의 이전 노드
                p = q.next # 삭제할 노드

                q.next = p.next
                self.size -= 1

                return p.data
        else:
            print('Underflow.')


    def printList(self):
        p = self.head # p, q; node들 순회하는 화살표

        while p != None:
            print('[%s] -> ' % (p.data), end='')
            p = p.next
        print('\b\b\b    ') # \b: 백스페이스


if __name__=='__main__':
    L = ListType() # 비어 있는 리스트 만들기

    L.insertFirst('A'); L.printList()
    L.insertFirst('B'); L.printList()

    L.insert(2, 'C'); L.printList()
    L.insert(4, 'D'); L.printList()
    L.insert(1, 'E'); L.printList()

    print('[%c] is deleted.' % L.deleteFirst()); L.printList()
    print('[%c] is deleted.' % L.delete(3)); L.printList()







