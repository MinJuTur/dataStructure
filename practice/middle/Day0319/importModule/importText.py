import FindMinMax, Sumrange # 사용자가 정의한 모듈도 import 할 수 있음
import random

A = []
for _ in range(10):
    A.append(random.randint(1, 100))

print("(min, max) =", FindMinMax.find_min_max(A))
print("Sum =", Sumrange.sum_range(1, 10))

