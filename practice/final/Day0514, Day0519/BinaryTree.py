import queue

class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None # 공집합 트리로 시작

    def preOrder(self, root): # 전위 순회
        if root != None:
            print('[%c] '% root.data, end='')
            self.preOrder(root.left)
            self.preOrder(root.right)

    def inOrder(self, root): # 중위 순회
        if root != None:
            self.inOrder(root.left)
            print('[%c] '% root.data, end='')
            self.inOrder(root.right)

    def postOrder(self, root): # 후위 순회
        if root != None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print('[%c] '% root.data, end='')

    def levelOrder(self, root): # 레벨 순회(BFS와 동일)
        Q = queue
        Q.put(root)
        while not Q.Empty():
            root = Q.get() # 꺼내서
            print('[%c] '% root.data, end='') # 방문

            # 루트 노드의 왼쪽, 오른쪽 노드를 큐에 넣기
            if root.left != None:
                Q.put(root.left)
            if root.right != None:
                Q.put(root.right)

    def nodeCount(self, root): # 전체 노드 수
        if root == None:
            return 0
        else:
            return 1 + self.nodeCount(root.left) + self.nodeCount(root.right) # 순환 호출

    def isExternal(self, root): # 노드가 외부 노드인지
        return root.left == None and root.right == None


    def leafNodeCount(self, root): # 단말 노드 수
        if root == None:
            return 0
        else:
            if self.isExternal(root): # 외부 노드
                return 1
            else: # 내부 노드
                return self.leafNodeCount(root.left) + self.leafNodeCount(root.right)

    def getHeight(self, root): # 트리의 높이(매우 중요!)
        if root == None:
            return 0
        else:  # 트리의 높이는 레벨의 최댓값 => 1 + Max(왼쪽 서브트리 높이, 오른쪽 서브트리 높이)
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def treeReverse(self, root):
        if root != None:
            root.left, root.right = root.right, root.left
            self.treeReverse(root.left)
            self.treeReverse(root.right)


if __name__ == '__main__':
    T = BinaryTree()

    N6 = Node('F')
    N5 = Node('E')
    N4 = Node('D')
    N3 = Node('C', N6, None)
    N2 = Node('B', N4, N5)
    N1 = Node('A', N2, N3)

    # Traversal 함수
    print('Pre : ', end=''); T.preOrder(N1); print()
    print('In : ', end=''); T.inOrder(N1); print()
    print('Post : ', end=''); T.postOrder(N1); print()

    print('Num of Nodes : %d' % T.nodeCount(N1))
    print('Num of Leaves : %d' % T.leafNodeCount(N1))
    print('Tree Height : %d' % T.getHeight(N1))

    T.treeReverse(N1)
    print('Pre : ', end=''); T.preOrder(N1); print()
    print('In : ', end=''); T.inOrder(N1); print()
    print('Post : ', end=''); T.postOrder(N1); print()
    print('Level : ', end=''); T.levelOrder(N1); print()
