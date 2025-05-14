class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None # 공집합 트리로 시작


if __name__ == '__main__':
    T = BinaryTree()

    N6 = Node('F')
    N5 = Node('E')
    N4 = Node('D')
    N3 = Node('C', N6, None)
    N2 = Node('B', N4, N5)
    N1 = Node('A', N2, N3)

    # Traversal 함수
