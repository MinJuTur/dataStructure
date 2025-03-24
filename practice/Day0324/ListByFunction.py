capacity = 100
size = 0
array = [None] * capacity # 인덱스: 0~99

def isEmpty():
    return size == 0

def isFull():
    return size == capacity

def insert(pos, e):
    global size
    if not isFull() and 0 <= pos <= size: # pos는 size까지 포함돼야 함
        for i in range(size, pos, -1):
            array[i] = array[i-1]
        array[pos] = e
        size += 1
    else:
        print("Overflow or Invalid Position.")

def delete(pos):
    global size
    if not isEmpty() and 0 <= pos < size:
        e = array[pos]
        for i in range(pos,size-1):
            array[i] = array[i+1]
        size -= 1
        return e
    else:
        print("Underflow or Invalid Position.")

def getEntry(pos):
    if (0 <= pos < size):
        return array[pos]
    else:
        return None


if __name__ == '__main__':
    insert(0, 'A')
    insert(1, 'B')
    insert(1, 'C')
    print(array[0:size])

    insert(4, 'D')
    insert(3, 'E')
    print(array[0:size])

    print('Deleted : %c' % delete(1))
    print(array[0:size])