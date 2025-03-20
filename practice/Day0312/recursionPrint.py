def rPrint(num):
    if num < 10:
        print(num)
    else:
        rPrint(num // 10)
        print(num%10)
        
n = int(input("양의 정수를 입력: " ))
rPrint(n)