import queue # 파이썬의 queue 모듈

# 큐 클래스
Q = queue.Queue(maxsize=20)

for i in range(1,10):
    Q.put(i)

print('Queue : ', end=' ')

for i in range(1,10):
    print(Q.get(), end=' ')
print()


# 스택 클래스
S = queue.LifoQueue(maxsize=20)

for i in range(1, 10):
    S.put(i)

print('Stack : ', end=' ')

for i in range(1,10):
    print(S.get(), end=' ')
print()


