class TreeNode:
    def __init__(self, key): # 새로 생기는 노드는 단일 노드이므로 key만 받음
        self.key = key
        self.left = None
        self.right = None

# 일반 함수들
def insert(root, key):
    if root == None:
        return TreeNode(key)

    # 탐색 작업
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else: # 중복된 키를 찾았을 때 -> 삽입하지 않음
        pass

    return root # root 노드 반환 == 서브 트리를 반환

def getMin(root): # 가장 작은 키 값을 가지는 노드 찾기
    while root != None and root.left != None:
        root = root.left

    return root

def delete(root, key):
    if root == None: # 못 찾았을 때 -> 삭제할 것이 없음
        return None

    # 탐색 작업
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else: # 삭제할 노드를 발견했을 때
        if root.left == None: # 왼쪽 서브트리가 없는 경우(Case1)
            return root.right
        elif root.right == None: # 왼쪽 서브트리만 있는 경우(Case2)
            return root.left
        else: # 두 개의 자식 노드를 모두 가지는 경우(Case3): 계승자 찾기
            succ = getMin(root.right) # 계승자: 삭제할 노드를 대체할 노드 찾기 -> 가장 큰 놈들 중 가장 작은 놈 찾기
            root.key = succ.key # 삭제할 노드를 계승자로 대체
            root.right = delete(root.right, succ.key) # 계승자인 노드 삭제하기

    return root # root 노드 반환 == 서브 트리를 반환


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
    data = [35, 18, 7, 26, 3, 22, 30, 12, 26, 68, 99]

    for key in data:
        root = insert(root, key)
        display(root, '[Insert %2d] : ' % key)
    print()

    root = delete(root, 30)
    display(root, '[Delete 30] : ')

    root = delete(root, 26)
    display(root, '[Delete 26] : ')

    root = delete(root, 18)
    display(root, '[Delete 18] : ')
