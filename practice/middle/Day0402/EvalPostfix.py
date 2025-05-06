from practice.middle.Day0331.ArrayStack import ArrayStack

def evalPostfix(expr):
    S = ArrayStack()

    for term in expr:
        if term in '+-*/': # 연사자일 때
            val2 = S.pop() # 연산의 오른쪽
            val1 = S.pop() # 연산의 왼쪽

            if term == '+':
                S.push(val1 + val2)
            elif term == '-':
                S.push(val1 - val2)
            elif term == '*':
                S.push(val1 * val2)
            elif term == '/':
                S.push(val1 / val2)
        else:
            S.push(float(term)) # 피연산자일 때

    return S.pop()

if __name__ == '__main__':
    str = '8 2 / 3 - 3 2 * +'
    expr = str.split() # 공백을 기준으로 나눠 리스트로 만들기
    print(str, '--->', evalPostfix(expr))

