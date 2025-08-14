# deep copy of binary Tree

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None


# preorder traversal
def copyTree(root : TreeNode) -> TreeNode:

    if(not root):
        return None
    
    copyNode = TreeNode(root.val)
    copyNode.left = copyTree(root.left)
    copyNode.right = copyTree(root.right)
    return copyNode