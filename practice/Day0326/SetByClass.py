class ArraySet:

    def __init__(self, capacity=100):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def __str__(self):
        return str(self.array[0:self.size])

    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
        return False # 반복문을 빠져나왔다는 것은 못 찾았다는 것임

    def insert(self, e):
        if not self.contains(e) and not self.isFull():
            self.array[self.size] = e
            self.size += 1

    def delete(self, e): #집합에서는 위치로 접근하지 않음
        for i in range(self.size):
            if (self.array[i] == e):
                self.array[i] = self.array[self.size-1] # 순서가 없기 때문에 가장 마지막 원소가 삭제된 위치에 채워짐
                self.size -= 1
                return  # 종료

    def union(self, other): # 하나의 객체가 다른 객체를 불러야 함
        resultSet = ArraySet()

        for i in range(self.size):
            resultSet.insert(self.array[i])

        for i in range(other.size):
            if not resultSet.contains(other.array[i]):
                resultSet.insert(other.array[i])

        return resultSet

    def intersect(self, other):
        resultSet = ArraySet()

        for i in range(self.size):
            if other.contains(self.array[i]):
                resultSet.insert(self.array[i])

        return resultSet

    def difference(self, other):
        resultSet = ArraySet()

        for i in range(self.size):
            if not other.contains(self.array[i]): # 차집합은 겹치지 않는 원소들의 집합
                resultSet.insert(self.array[i])

        return resultSet

if __name__ == '__main__':
    S = ArraySet(20)
    S.insert(10)
    S.insert(30)
    S.insert(20)
    S.insert(30)
    S.insert(40)
    print('S =', S)

    T = ArraySet(20)
    T.insert(40)
    T.insert(50)
    T.insert(20)
    T.insert(10)
    T.insert(60)
    print('T =', T)

    T.delete(10)
    print('T =', T)

    print('S U T =', S.union(T))
    print('S ∩ T =', S.intersect(T))
    print('S - T =', S.difference(T))


