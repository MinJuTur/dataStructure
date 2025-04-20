from CircularQueue import CircularQueue

map = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '1', '0', '0', '1'],
    ['1', '0', '0', '0', '1', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '0', '1', '0', '0', 'x'],
    ['1', '1', '1', '1', '1', '1']
]

SIZE = 6

def isValidPos(r, c):
    if 0 <= r < SIZE and 0 <= c < SIZE:
        if map[r][c] == '0' or map[r][c] == 'x':
            return True

    return False

def BFS(): # 너비우선탐색
    Q = CircularQueue()
    Q.enqueue((1,0))
    print('BFS : ')

    while not Q.isEmpty():
        pos = Q.dequeue()
        (r, c) = pos
        print(pos, end=' - > ') # 현재 방문한 위치

        if (map[r][c] == 'x'):
            return True
        else:
            map[r][c] = '.' # 방문 표시, 이후 더 이상 안 간다는 표시
            if isValidPos(r-1, c):  Q.enqueue((r-1, c)) # 위
            if isValidPos(r+1, c): Q.enqueue((r+1, c)) # 아래
            if isValidPos(r, c-1): Q.enqueue((r, c-1)) # 왼쪽
            if isValidPos(r, c+1): Q.enqueue((r, c+1)) # 오른쪽

        # print(Q.array[Q.front+1:Q.rear+1]) 방문할 수 있는 위치
        print_queue(Q)

    return False

def print_queue(Q):
    result = []
    i = Q.front
    while i != Q.rear:
        i = (i + 1) % Q.capacity
        result.append(Q.array[i])
    print(result)

if __name__ == '__main__':
    result = BFS()

    if result:
        print('Success')
    else:
        print('Fail')
