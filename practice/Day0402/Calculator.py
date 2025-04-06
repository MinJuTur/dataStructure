from EvalPostfix import evalPostfix
from InfixToPostfix import infixToPostfix

infix = input('수식을 입력 : ')
expr = infix.split()

print(infix, '=', evalPostfix(infixToPostfix(expr)))
