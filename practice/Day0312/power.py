def iPower(x,n):
    result = 1

    for _ in range(n):
        result *= x

    return result

def rPower(x, n): # 분할 정복 (n을 절반씩 나눔)
    if n == 0:
        return 1
    elif (n % 2) == 0:
        return rPower(x*x,n//2)
    else:
        return x * rPower(x*x, (n-1)//2)

def Power(x, n): # 단순 재귀
    if n==0:
        return 1
    else:
        return x*Power(x,n-1)


print('iPower : %d' % (iPower(2, 10)))
print('rPower : %d' % (rPower(2, 10)))
print('Power : %d' % (Power(2, 10)))