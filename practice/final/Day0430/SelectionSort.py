def printStep(A, idx):
    print('  Step %d  : ' % idx, end='')
    print(A)
    
def selectionSort(A): # 선택 정렬 알고리즘
    n = len(A)
    # 가장 왼쪽 값을 최소값으로 산정해놓고 그 이후 리스트 요소들을 비교

    for i in range(n-1):  # outer loop: 가장 왼쪽 요소 최소값으로 산정(0부터 n-2까지)
        minIdx = i
        for j in range(i+1, n): # inner loop: 그 이후 리스트 요소들 비교(1부터 n-1까지)
            if A[j] < A[minIdx]:
                minIdx = j
        A[i], A[minIdx] = A[minIdx], A[i] # 위치 교환
        printStep(A, i+1)


if __name__ == '__main__':
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]

    L = list(data)
    print("Before    :", L)
    selectionSort(L)
    print("Selection :", L)
    print()