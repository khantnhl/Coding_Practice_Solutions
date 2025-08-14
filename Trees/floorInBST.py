class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
def floorInBST(root : TreeNode, target : int) -> TreeNode:

    if(not root):
        return None
    
    curr = root
    floor = -1

    while(curr):
        if(curr.val == target):
            return curr.val
        
        if(target < curr.val):
            curr = curr.left
        else:
            floor = curr.val
            curr = curr.right
    return floor