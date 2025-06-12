# 개방 주소법
M = 13 # 버킷 사이즈(소수로)

class HashTable:
    def __init__(self):
        self.table = [0] * M

    def hashFn(self, key):
        return key % M   # 제산법

    def hashFn2(self, key): # 이중 해싱법
        return 11 - (key % 11) # 공식, M보다 작은 소수 중 가장 큰 소수

    def insert(self, key): # 삽입 연산
        hashVal = self.hashFn(key) # 해시 값 구하기

        for i in range(M): # 최대 M번 시도, 빈 자리가 있을 때까지
            # bucket = (hashVal + i) % M  # Linear proving(선형 조사법)
            # bucket = (hashVal + i**2) % M  # Quadratic proving(이차 조사법)
            bucket = (hashVal + i*self.hashFn2(key)) % M # Double Hashing(이중 해싱법)

            if self.table[bucket] == 0: # 빈 방일 때
                self.table[bucket] = key
                break

    def search(self, key): # 탐색 연산
        hashVal = self.hashFn(key) # 해시 값 구하기

        for i in range(M):
            # bucket = (hashVal + i) % M  # Linear proving(선형 조사법)
            # bucket = (hashVal + i**2) % M  # Quadratic proving(이차 조사법)
            bucket = (hashVal + i*self.hashFn2(key)) % M # Double Hashing(이중 해싱법)

            if self.table[bucket] == 0: # 빈 방일 때(그 이후 방에도 없다는 뜻)
                return -1
            elif self.table[bucket] == key: # 찾았을 때
                return bucket

    def delete(self, key): # 삭제 연산
        hashVal = self.hashFn(key) # 해시 값 구하기

        for i in range(M):
            # bucket = (hashVal + i) % M  # Linear proving(선형 조사법)
            # bucket = (hashVal + i**2) % M  # Quadratic proving(이차 조사법)
            bucket = (hashVal + i*self.hashFn2(key)) % M # Double Hashing(이중 해싱법)

            if self.table[bucket] == 0: # 빈 방일 때(그 이후 방에도 없다는 뜻)
                print("No key to delete.")
                return -1
            elif self.table[bucket] == key: # 찾았을 때
                print("Delete Key(%d) at bucket(%d)." % (key, bucket))
                self.table[bucket] = -1 # 0: 원래부터 빈 방, -1: 있었다가 삭제된 상태 (구분해줘야 함)
                return bucket

    def display(self):
        print('\nBucket    Key')
        print('=============')

        for i in range(M):
            print('HT[%2d] :  %2d' % (i, self.table[i]))

if __name__ == '__main__':

    HT = HashTable()
    data = [45, 27, 88, 9, 71, 60, 46, 38, 24]
    # data = [10, 20, 30, 40, 33, 46, 50, 60]

    for d in data:
        print('h(%d)=%2d' % (d, HT.hashFn(d)), end=' ')
        HT.insert(d)
        print(HT.table)

    HT.display(); print()

    print('Search(46) ---> ', HT.search(46))
    HT.delete(9); HT.display(); print()

