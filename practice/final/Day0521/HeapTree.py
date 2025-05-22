N = 20

class MaxHeap:
    def __init__(self):
        self.heap = [None] * N  # 배열로 표현
        self.heapSize = 0  # 배열의 인덱스 번호를 의미

    def upHeap(self): 
        i = self.heapSize # 처음 시작 위치
        key = self.heap[i]

        while (i != 1) and (key > self.heap[i // 2]): # 부모 노드가 존재하고 부모 노드의 키 값보다 클 때
            self.heap[i] = self.heap[i // 2] # 부모 노드와 교환
            i = i // 2
        self.heap[i] = key

    def insertItem(self, item): # 삽입 연산
        self.heapSize += 1
        self.heap[self.heapSize] = item # 완전이진트리 조건 만족
        self.upHeap() # 크기 비교 조건 만족

    def downHeap(self):
        p = 1  # 처음 시작 위치: 루트 노드
        c = 2  # 자식 노드 위치
        key = self.heap[p]

        while c <= self.heapSize: # 비교할 자식 노드가 존재할 때
            # 오른쪽 자식까지 있을 때, and 오른쪽 자식이 더 클 때 -> 부모는 오른쪽 자식과 비교
            if (c < self.heapSize) and (self.heap[c+1] > self.heap[c]):
                c += 1

            if key >= self.heap[c]:
                break
            self.heap[p] = self.heap[c]
            p = c
            c *= 2
        self.heap[p] = key

    def deleteItem(self): # 삭제 연산
        key = self.heap[1] # 루트 노드의 키 값
        self.heap[1] = self.heap[self.heapSize] # 맨 마지막 노드와 교환
        self.heapSize -= 1 # 맨 마지막 노드 삭제 -> 완전이진트리 조건 만족
        self.downHeap()
        return key
    
if __name__ == '__main__':
    H = MaxHeap()
    data = [9, 7, 6, 5, 4, 3, 2, 2, 1, 3]

    for e in data:
        H.insertItem(e)
        print('Heap :', H.heap[1:H.heapSize + 1])

    H.insertItem(8)
    print('Heap :', H.heap[1:H.heapSize + 1])
    print()

    print('[%d] is deleted.' % H.deleteItem())
    print('Heap :', H.heap[1:H.heapSize + 1])

