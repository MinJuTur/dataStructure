class Poly: # 다항식 만들기

    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.degree = 0 # 다항식의 차수
        self.coefArr = [None] * capacity # 다항식의 계수 저장 배열

    def readPoly(self):
        self.degree = int(input('다항식의 차수를 입력: '))
        for i in range(self.degree, -1, -1): # 다항식의 차수 ~ 0까지 감소
            coef = int(input(' %d차 항의 계수 : ' % i))
            self.coefArr[i] = coef # i차 항의 계수는 배열의 i번째 인덱스에 저장

    def printPoly(self):
        for i in range(self.degree, 0, -1): # n차~1차 출력
            if (self.coefArr[i] == 0): # 계수가 0이면 출력하지 않음
                continue
            print('%dx^%d + ' % (self.coefArr[i], i), end='')
        print(self.coefArr[0]) # 상수항 출력

    def add(self, other):   # 다항식 더하기
        if (self.degree >= other.degree):
            larger = self
            smaller = other
        else:
            larger = other
            smaller = self

        sumPoly = Poly(larger.degree+1)
        sumPoly.degree = larger.degree

        for i in range(sumPoly.degree+1):
            if (i > smaller.degree):
                smallerCoef = 0
            else:
                smallerCoef = smaller.coefArr[i]
            largerCoef = larger.coefArr[i]

            sumPoly.coefArr[i] = smallerCoef + largerCoef

        return sumPoly


    def evaluate(self, x):
        sum = 0
        for i in range(self.degree, -1, -1):
            sum += self.coefArr[i] * (x ** i)
        return sum

if __name__ == '__main__':
    a = Poly()
    a.readPoly()
    print('a =', end="")
    a.printPoly()

    b = Poly()
    b.readPoly()
    print('b =', end="")
    b.printPoly()

    print('a + b =', end="")
    c = a.add(b)
    c.printPoly()

    print('a(-1) =', a.evaluate(-1))
    print('b(2) =', b.evaluate(2))

