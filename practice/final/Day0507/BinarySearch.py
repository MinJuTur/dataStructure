import random

def seqSearch(A, key): # 순차 탐색(정렬되지 않은 배열)
    n = len(A)

    for i in range(n):
        if A[i] == key:
            return i
    return -1

def insertionSearch(A): # 삽입 정렬
    n = len(A)
    
    for i in range(1, n): # 첫 번째 카드는 이미 왼손에 있는 상태
        key = A[i] # 오른손에 든 카드
        j = i - 1 # 왼손에 있는 카드

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key

def iBinarySearch(A, key): # 반복문 사용한 이진 탐색(정렬된 배열)
    low = 0
    high = len(A) - 1

    while (low <= high): # 탐색할 값이 있는 동안 반복
        mid = (low + high) // 2
        print(A[mid], end=' ') # 확인용 출력 optional

        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

def rBinarySearch(A, key, low, high): # 함수 호출을 이용한 이진 탐색(정렬된 배열) -> 찾을 범위를 파라미터로 받아야 함
    if low <= high: # 탐색할 값이 남아있는 동안
        mid = (low + high) // 2
        print(A[mid], end=' ') # 확인용 출력 optional

        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return rBinarySearch(A, key, low, mid-1)
        else:
            return rBinarySearch(A, key, mid+1, high)

    return -1

if __name__ == '__main__':
    A = []
    for i in range(15):
        A.append(random.randint(1, 100))

    insertionSearch(A)
    print('A[] =', A)


    key = int(input("Input Search Key : "))
    #idx = seqSearch(A, key)
    #idx = iBinarySearch(A, key)
    idx = rBinarySearch(A, key, 0, 14)

    print()
    if idx != -1:
        print('found in %d position.' % idx)
    else:
        print('Key is Not found.')