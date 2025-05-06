from practice.middle.Day0331.ArrayStack import ArrayStack

def order(op): # 연산자 우선순위 계산하는 함수
    if (op == '(' or op == ')'): return 0
    elif (op == '+' or op == '-'): return 1
    else: return 2


def infixToPostfix(expr): # 중위 표기식 -> 후위 표기식
    S = ArrayStack()
    postfix = []

    for term in expr:
        if term in '(':
            S.push(term)
        elif term in ')':
            while not S.isEmpty(): # 왼쪽 괄호를 만날 때까지 꺼내기
                op = S.pop()
                if op == '(':
                    break
                else:
                    postfix.append(op)
        elif term in '+-*/':
            while not S.isEmpty():
                op = S.peek()
                if (order(term) <= order(op)): # 스택에 있는 연산자의 우선순위가 더 크거나 같다면
                    postfix.append(S.pop())
                else: break
            S.push(term)
        else: # 피연산자일 때
            postfix.append(term)

    while not S.isEmpty():
        postfix.append(S.pop())

    return postfix


if __name__ == '__main__':
    infix = input('수식을 입력하세요 : ')
    expr = infix.split()
    postfix = infixToPostfix(expr)

    print(postfix)