class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def getHeight(root):
    if root == None:
        return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))

def getBalance(root):
    if root is None:
        return 0
    return getHeight(root.left)-getHeight(root.right)

def rotateLeft(p):
    c = p.right # p: 부모 노드, c: 자식 노드 가리킴
    p.right = c.left # 자식 노드의 왼쪽 서브트리를 부모의 오른쪽 서브트리로 위임
    c.left = p
    return c

def rotateRight(p):
    c = p.left # p: 부모 노드, c: 자식 노드 가리킴
    p.left = c.right # 자식 노드의 왼쪽 서브트리를 부모의 오른쪽 서브트리로 위임
    c.right = p
    return c


def insert(root, key):
    if root == None:
        return TreeNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        pass
    # 추가
    balance = getBalance(root) # 균형인수

    # 균형이 깨지는 경우 네 가지
    if balance > 1 and key < root.left.key: # LL
        print('--- LL Type ---')
        return rotateRight(root)
    if balance > 1 and key > root.left.key: # LR
        print('--- LR Type ---')
        root.left = rotateLeft(root.left) # 왼쪽 서브트리의 모양을 바꾸기(LR로 바꿈)
        return rotateRight(root)
    if balance < -1 and key > root.left.key: # RL
        print('--- RL Type ---')
        root.right = rotateRight(root.right) # 오른쪽 서브트리의 모양을 바꾸기(RR로 바꿈)
        return rotateLeft(root)
    if balance < -1 and key > root.right.key: # RR
        print('--- RR Type ---')
        return rotateLeft(root)
    return root

def preOrder(root):
    if root != None:
        print('%2d ' % root.key, end='')
        preOrder(root.left)
        preOrder(root.right)

def display(root, msg):
    print(msg, end='')
    preOrder(root)
    print()

if __name__ == '__main__':
    root = None
    data = [7, 8, 9, 2, 1, 5, 3, 6, 4]  # 리스트를 보고 트리의 모양 고르기 문제 출제

    for i in range(9):
        root = insert(root, data[i])
        display(root, '[Insert %2d] : ' % data[i])
    print()
