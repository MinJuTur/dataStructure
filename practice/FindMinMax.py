import random

def find_min_max(A):
    min = max = A[0]
    
    for i in range(1, len(A)):
        if max < A[i]:
            max = A[i]
        if min > A[i]:
            min = A[i]
    
    return (min, max)

if __name__ == '__main__': #FindMinMax 모듈을 실행시키는 것이 자기 자신일 때 실행, importText가 실행시키는 경우 실행되지 않음
    A = []
    for _ in range(10):
        A.append(random.randint(1, 100))

    print(A)
    print(find_min_max(A))
