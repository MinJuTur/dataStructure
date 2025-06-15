# 체이닝
M = 13

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class HashTable:
    def __init__(self):
        self.table = [None] * M  # 헤드 포인터 배열

    def hashFn(self, key):
        return key % M

    def insert(self, key):
        bucket = self.hashFn(key)
        node = Node(key)
        node.next = self.table[bucket] # 누굴 가리키지? 헤드 포인터가 가리키는 노드를 가리킴
        self.table[bucket] = node # 누가 날 가리키지? 헤드 포인터가 나를 가리킴

    # def search(self, key):
    #     bucket = self.hashFn(key)
    #     n = self.table[bucket]
    #
    #     while n is not None:
    #         if n.data == key:
    #             return bucket
    #         n = n.next
    #     return -1
    #
    # def delete(self, key):
    #     bucket = self.hashFn(key)
    #     curr = self.table[bucket]
    #     prev = None
    #
    #     while curr is not None:
    #         if curr.data == key:
    #             if prev is None: # 삭제 대상이 첫번째 노드일 때
    #                 self.table[bucket] = curr.next
    #             else:
    #                 prev.next = curr.next
    #             return bucket
    #         prev = curr
    #         curr = prev.next
    #
    #     return -1

    def display(self):
        for i in range(M):
            print('HT[%02d] : ' % (i), end='')
            n = self.table[i]

            while n is not None:
                print(n.data, end=' ')
                n = n.next

            print()

if __name__=='__main__':
    import random

    HT = HashTable()

    for i in range(20):
        HT.insert(random.randint(10, 99))

    HT.display()