Graph = {  # 가중치 그래프
    'A':[('B', 29), ('F', 10)],
    'B':[('A', 29), ('C', 16), ('G', 15)],
    'C':[('B', 16), ('D', 12)],
    'D':[('C', 12), ('E', 22), ('G', 18)],
    'E':[('D', 22), ('F', 27), ('G', 25)],
    'F':[('A', 10), ('E', 27)],
    'G':[('B', 15), ('D', 18), ('E', 25)]
}

INF = 1000  # 임의의 큰 값
dist = [INF] * len(Graph)
visited = [False] * len(Graph)

def findMin():
    minDist = INF
    minV = 0 # 0번 정점을 최솟값 정점으로 놓고 시작
    for v in range(len(dist)):
        if visited[v] == False and dist[v] < minDist:
            minDist = dist[v]
            minV = v

    return minV

def prim(vName): # Prim 알고리즘
    vCnt = len(Graph) # 정점의 개수
    dist[ord(vName)-65] = 0
    for i in range(vCnt):
        vNum = findMin()
        vName = chr(vNum + 65)

        for j in range(vCnt): # dist 배열이 업데이트 되는 과정(*: INF)
            if dist[j] == INF:
                print("  * ", end='')
            else:
                print('%3d ' % dist[j], end='')
        print()

        visited[vNum] = True
        # print('[%c(%d)] ' % (vName, dist[vNum]), end='')

        for e in Graph[vName]: # 현재 정점의 인접 노드 탐색
            vNum = ord(e[0]) - 65
            # 아직 방문하지 않은 인접 노드의 가중치가 최소가 되도록 업데이트
            if visited[vNum] == False and e[1] < dist[vNum]:
                dist[vNum] = e[1]

    # dist[vName-'A'] = 0 도 가능한가?

if __name__ == '__main__':
    prim('C')


