"""
time : O(height + k)
space: O(log(N) + k)
"""

def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    stack = []

    while root or stack:
        if(root):
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()

            k-=1
            if(k==0):
                return root.val

            root = root.right
        