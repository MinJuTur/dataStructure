Graph = {  # 가중치 그래프 -> 딕셔너리로 표현 + 튜플 리스트
    'A':[('B', 29), ('F', 10)],
    'B':[('A', 29), ('C', 16), ('G', 15)],
    'C':[('B', 16), ('D', 12)],
    'D':[('C', 12), ('E', 22), ('G', 18)],
    'E':[('D', 22), ('F', 27), ('G', 25)],
    'F':[('A', 10), ('E', 27)],
    'G':[('B', 15), ('D', 18), ('E', 25)]
}

def weightSum(): # 중요한 함수는 아님, 접근 테스트 위해
    sum = 0
    for v in Graph: # v: 키
        for e in Graph[v]: # e: 키에 해당하는 튜플
            sum += e[1]

    return sum // 2  # 가중치 총합(중복이 되어 있으므로 2로 나눔)

def display():
    for v in Graph:
        for e in Graph[v]:
            if v < e[0]: # 사전 상 먼저 나올 때만 출력(중복 제거)
                print('[%s%s %d] ' % (v, e[0], e[1]), end='')
        print()


if __name__ == '__main__':
    print('Total Weight =', weightSum())
    display()