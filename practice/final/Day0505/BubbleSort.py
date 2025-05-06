def printStep(A, idx):
    print('   Step %d : ' % idx, end='')
    print(A)

def bubbleSort(A): # 버블 정렬 알고리즘
    n = len(A)

    for i in range(n-1):
        flag = False

        for j in range(1, n-i): # 작업 범위
            if (A[j-1] > A[j]):
                A[j-1], A[j] = A[j], A[j-1] # 교환
                flag = True # 정렬한 것이 있었다

        if not flag: # 전체 범위에서 정렬한 것이 없었다 = 이미 정렬되었다
            break

        printStep(A, i+1)


if __name__ == '__main__':
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]

    L = list(data)
    print("Before    :", L)
    bubbleSort(L)
    print("Bubble    :", L)
    print()