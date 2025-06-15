vName = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
visited = [False] * len(vName) # 방문 기록

AdjVer = [ # 연결된 정점만 표현
    [1,2],
    [0,3],
    [0,3,4],
    [1,2,5],
    [2,6,7],
    [3],
    [4,7],
    [4,7]
]

# 명시적 스택 사용 -> 깊이 우선 탐색
from queue import LifoQueue

class Stack(LifoQueue): # 내가 정의한 스택 -> peek 추가
    def peek(self):
        if not self.empty():
            return self.queue[-1]
        raise Exception("Stack is Empty")

def iDfs(s): # 반복문
    S = Stack()

    S.put(s)
    visited[s] = True  # 방문 기록 남기기
    print('[%s] ' % vName[s], end='')

    while not S.empty():
        s = S.peek() # 아예 꺼내버리면 안 됨(다시 돌아와야 하므로)
        flag = False # 더 이상 방문할 정점이 있는지

        for t in AdjVer[s]: # t: s와 연결된 정점
            if visited[t] == False: # 방문을 안 했다면
                # t 방문하기(깊이 우선 탐색이므로)
                S.put(t)
                visited[t] = True  # 방문 기록 남기기
                print('[%s] ' % vName[t], end='')

                flag = True
                break

        if flag == False:  # 반복문 안에서 아무일도 일어나지 않았을 때
            S.get() # 해당 정점 지우기

if __name__ == '__main__':
    print('iDFS : ', end='')
    iDfs(1)

