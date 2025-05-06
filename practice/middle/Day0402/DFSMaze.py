from practice.middle.Day0331.ArrayStack import ArrayStack

map = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '0', '0', '0', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '1', '1', '0', '0', 'x'],
       ['1', '1', '1', '0', '1', '1'],
       ['1', '1', '1', '1', '1', '1']]

SIZE = 6

def isValidPos(r, c):
    if 0 <= r < SIZE and 0 <= c < SIZE:
        if map[r][c] == '0' or map[r][c] == 'x':
            return True

    return False

def DFS():
    print('DFS : ')
    S = ArrayStack()
    S.push((1,0)) # 입구, 처음 시작점

    while not S.isEmpty(): # 갈 수 있는 길이 있을 때
        pos = S.pop()
        (r, c) = pos
        print(pos, end=' -> ')

        if (map[r][c] == 'x'):
            return True
        else:
            map[r][c] = '.' # 방문 표시, 이후 더 이상 안 간다는 표시
            if isValidPos(r-1, c): S.push((r-1, c)) # 위
            if isValidPos(r+1, c): S.push((r+1, c)) # 아래
            if isValidPos(r, c-1): S.push((r, c-1)) # 왼쪽
            if isValidPos(r, c+1): S.push((r, c+1)) # 오른쪽

        print(S.array[S.top::-1])

    return False # 반복문을 빠져나왔는데도 못 찾은 경우

if __name__ == '__main__':
    result = DFS()

    if result:
        print('Success')
    else:
        print('Fail')

