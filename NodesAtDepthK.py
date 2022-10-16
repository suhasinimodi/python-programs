class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def treeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def PrintTree(root):
    if root == None:
        return
    print(root.data,end= ":")
    if root.left is not None:
        print("L", root.left.data, end = ",")
    if root.right is not None:
        print("R", root.right.data, end = "")
    print()
    PrintTree(root.left)
    PrintTree(root.right)
#Approach 1
def PrintDepthK(root,k):
    if root is None:
        return
    if k == 0:
        print(root.data)
        return
    PrintDepthK(root.left,k-1)
    PrintDepthK(root.right,k-1)
#Approach 2
def PrintDepthKv2(root,k,d = 0):
    if root is None:
        return
    if k == d:
        print(root.data)
        return
    PrintDepthKv2(root.left,k,d+1)
    PrintDepthKv2(root.right,k,d+1)

root = treeInput()
PrintTree(root)
PrintDepthKv2(root,2)
