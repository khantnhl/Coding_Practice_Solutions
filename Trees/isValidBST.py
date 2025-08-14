
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# (-inf, root) 
# (root, inf)
def isValidBST(root : TreeNode, val : int) -> TreeNode:
    if(not root):
        return None
    
    def valid(root, left, right):

        if(not root):
            return None
        
        if(left < root.data < right):
            return True
        
        # (rootleft, -inf, data) and (rootright, data, inf)
        return valid(root.left, left, root.data) and valid(root.right, root.data, right)
    
    return valid(root, float('-inf'), float('inf'))
