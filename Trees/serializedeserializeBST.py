
"""
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

serialize -> 1,2,N,N,3,N,N,4,N,N,5,N,N

"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        # do preorder traversal : root, left, right
        result = []
        def dfs(root):
            if(not root):
                result.append("N")
                return 

            result.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        self.idx = 0

        def dfs():
            if(nodes[self.idx]=="N"):
                self.idx += 1
                return None
            
            node = TreeNode(int(nodes[self.idx]))
            self.idx += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
     
