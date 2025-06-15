vName = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
visited = [False] * len(vName) # 방문 기록
Graph = [   # 인접 행렬
    [0,1,1,0,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,1,1,0,0,0],
    [0,1,1,0,0,1,0,0],
    [0,0,1,0,0,0,1,1],
    [0,0,0,1,0,0,0,0],
    [0,0,0,0,1,0,0,1],
    [0,0,0,0,1,0,1,0]
]

def printGraph():
    n = len(vName)
    print("    A  B  C  D  E  F  G  H")
    for i in range(n):
        print('%c |' % vName[i], end='')
        for j in range(n):
            print(' %d ' % Graph[i][j], end='')
        print(' |')

# 순환 호출
def rDfs(s): # s: 시작 정점
    visited[s] = True # 방문 기록 남기기
    print('[%s] ' % vName[s], end='')

    for t in range(len(vName)): # t: s입장에서 인접 정점
        if (Graph[s][t] == 1 and visited[t] == False): # 인접 정점과 연결되어 있고, 아직 방문하지 않았을 때
            rDfs(t)

if __name__ == '__main__':
    printGraph()
    print('\nrDFS : ', end='')
    rDfs(1)
