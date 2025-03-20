pi = 3.141592 # 전역 변수
perimeter = 0

def calc_perimeter(radius):
    global perimeter # 함수 내에서 전역 변수를 수정하기 위해서
    print("Pi : ", pi) # 함수 내에서 전역 변수 읽기는 가능
    perimeter = 2 * pi * radius # 함수 내에서 전역 변수 수정 -> 새로 선언된 지역 변수로 취급함(이름만 같은 서로 다른 변수)
    print(perimeter)

calc_perimeter(10)
print("Pi : ", pi)
print(perimeter) # perimeter로 0 출력
