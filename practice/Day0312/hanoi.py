def hanoi(n, fr, tmp, to):  # 원반번호, 시작 기둥, 보조 기둥, 목표 기둥
    if (n == 1):
        print("Disk %d : %s -- > %s" % (n, fr, to)) # A -> C
    else:
        # Step 1: n-1개를 보조 기둥 B로 이동 (C를 보조로 사용)
        hanoi(n - 1, fr, to, tmp) # A -> B

        # Step 2: 가장 큰 원반을 목표 기둥 C로 이동
        print("Disk %d : %s -- > %s" % (n, fr, to)) # A -> C

        # Step 3: B에 있는 n-1개를 C로 이동 (A를 보조로 사용)
        hanoi(n - 1, tmp, fr, to) # B -> C

hanoi(3, 'A', 'B', 'C')