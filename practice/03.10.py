def iFact(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

def rFact(n):
    if n==1:
        return 1
    else:
        return n*rFact(n-1)
    
print("iFact(6) = %d" %iFact(6))
print("rFact(6) = %d" %rFact(6))