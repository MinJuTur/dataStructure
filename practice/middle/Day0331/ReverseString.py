from ArrayStack import ArrayStack

S = ArrayStack(30) # 스택에 넣었다 빼면 문자열 거꾸로 출력 가능

str = input('Input String : ')
for c in str:
    S.push(c)

print('Print String : ', end='')
while not S.isEmpty(): # 스택이 비어있을 때까지
    print(S.pop(), end='')
print()



