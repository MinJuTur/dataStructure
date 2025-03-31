from ArrayStack import ArrayStack

def checkBrackets(str):
    S = ArrayStack(50)

    for c in str:
        if c == '[' or c == '{' or c == '(':
            S.push(c)
        elif c == ']' or c == '}' or c == ')':
            if S.isEmpty(): # 2번 조건 위배
                return False
            else:
                open = S.pop()
                if (c == ']' and open != '[') or \
                    (c == '}' and open != '{') or \
                    (c == ')' and open != '('): # 3번 조건 위배
                    return False

    return S.isEmpty() # 1번 조건 위배

if __name__ == '__main__':
    s1 = '{ A[(i+1)] = 0 }'
    s2 = 'if((i==0) && (j==0)'
    s3 = 'A[(i+1) = 0'

    print(s1, '-->', checkBrackets(s1))
    print(s2, '-->', checkBrackets(s2))
    print(s3, '-->', checkBrackets(s3))
