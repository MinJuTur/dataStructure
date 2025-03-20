class Car:

    def __init__(self, color, speed= 0): # 생성자
        self.color = color # 멤버 변수: 자동자 객체들이 가지고 있을 기본 특징, self는 각 객체를 의미함
        self.speed = speed # 앞에 self가 붙어 있지 않은 변수는 일반 변수임

    def speedUp(self): # 멤버 메서드
        self.speed += 10

    def speedDown(self): # 멤버 메서드
        self.speed -= 10

    def __str__(self): # 메서드 재정의
        return "Color : %s, Speed : %d" % (self.color, self.speed)


if __name__ == '__main__':
    car1 = Car('Black', 0)
    car2 = Car('Red', 100)
    car3 = Car('Yellow')

    print(car1) # 메서드를 재정의하지 않고 객체를 출력하면 객체가 저장된 메모리 주소가 출력됨
    print(car2)

    car3.speedUp()
    print(car3)

