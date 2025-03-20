def hanoi(n, A, B, C): # 원반번호, 시작 기둥, 보조 기둥, 목표 기둥
    if (n == 1):
        print("Disk %d : %s -- > %s" %(n, A, C)) # A -> C 
    else:
        hanoi(n-1, A, C, B) # A -> B
        print("Disk %d : %s -- > %s" %(n, A, C))
        hanoi(n-1, B, A, C) # B -> C 

hanoi(3, 'A', 'B', 'C')