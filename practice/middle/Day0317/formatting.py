import random

for _ in range(10):
    print("%4d" %(random.randint(100, 10000))) # 숫자를 4자리로 표현

print("----------------")
    
print("%f" % 3.14) # %f: 소수점 6자리까지 표현하기기
print("%4.1f" % 13.18437) # 총 4자리(최소 폭)로 표현하되 소수점은 첫째 자리까지 표현하기기
print("%3.2f" % 1.1)
