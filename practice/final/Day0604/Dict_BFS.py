Graph = {  # 딕셔너리로 표현(키: 정점이름)
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','D','E'],
    'D':['B','C','F'],
    'E':['C','G','H'],
    'F':['D'],
    'G':['E','H'],
    'H':['E','G']
}

visited = {} # 빈 딕셔너리

from queue import Queue

def BFS(s): # 너비 우선 탐색
    Q = Queue()

    Q.put(s) # 시작정점 넣기
    visited[s] = True  # 'D':True 형태로 들어감
    print('[%c] ' % s, end='')

    while not Q.empty():
        s = Q.get()

        for t in Graph[s]:
            if t not in visited:
                Q.put(t)
                visited[t] = True 
                print('[%c] ' % t, end='')


if __name__ == '__main__':
    print('BFS : ', end='')
    BFS('D')