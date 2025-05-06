def printStep(A, idx):
    print('   Step %d : ' % idx, end='')
    print(A)

def insertionSort(A): # 삽입 정렬 알고리즘
    n = len(A)

    for i in range(1, n): # 0번째 장은 이미 정렬, 1~(n-1)장까지 순회
        key = A[i] # 오른손에 들고 있는 카드
        j = i - 1 # 왼손에 들고 있는 카드

        while j >= 0 and A[j] > key:
            A[j + 1] = A[j] # 오른쪽으로 이동
            j -= 1 # 그 다음 카드

        A[j + 1] = key

        printStep(A, i)



if __name__ == '__main__':
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]

    L = list(data)
    print("Before    :", L)
    insertionSort(L)
    print("Insertion :", L)
    print()