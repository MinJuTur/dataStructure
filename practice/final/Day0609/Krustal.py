Graph = {  # 가중치 그래프
    'A':[('B', 29), ('F', 10)],
    'B':[('A', 29), ('C', 16), ('G', 15)],
    'C':[('B', 16), ('D', 12)],
    'D':[('C', 12), ('E', 22), ('G', 18)],
    'E':[('D', 22), ('F', 27), ('G', 25)],
    'F':[('A', 10), ('E', 27)],
    'G':[('B', 15), ('D', 18), ('E', 25)]
}

eList = []  # 간선 리스트
vertices = [-1, -1, -1, -1, -1, -1, -1]  # 각 인덱스는 A~G, 값은 속한 집합 번호

def edgeSort(): # 간선 정렬
    for v in Graph: # 키 꺼내기
        for e in Graph[v]: # 튜플 꺼내기
            if v < e[0]: # 간선 표기가 중복되지 않도록
                eList.append([v, e[0], e[1]]) # 두 정점과 가중치 저장

    eList.sort(key=lambda e: e[2], reverse=True) # 가중치로 정렬, 역순(내림차순)으로 정렬(pop을 했을 때 작은 값부터 나오도록)

    for i in range(len(eList)-1, -1, -1):
        print('[%c%c%d] ' % (eList[i][0], eList[i][1], eList[i][2]), end='')
    print()

def find(vNum):
    while vertices[vNum] != -1:
        vNum = vertices[vNum]
    return vNum

def union(vNum1, vNum2):
    vertices[vNum2] = vNum1

def krustal():
    edgeSort() # 간선을 가중치 값으로 정렬하기

    eCnt = 0 # 선택한 간선의 개수
    vCnt = len(Graph) # 정점의 개수

    while eCnt < vCnt-1:
        e = eList.pop() # 가중치 작은 것부터 꺼내기

        vNum1 = find(ord(e[0])-65) # 어떤 집합에 속하는지 집합 번호 구하기
        vNum2 = find(ord(e[1])-65)

        if vNum1 != vNum2: # 서로 다른 집합에 속하는 정점일 때
            eCnt += 1
            print('%d. [%s%s %d]' % (eCnt, e[0], e[1], e[2]))
            union(vNum1, vNum2) # 같은 집합으로 만들기

if __name__ == '__main__':
    krustal()

