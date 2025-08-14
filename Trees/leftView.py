class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None

from collections import deque

def leftView(root : TreeNode) -> list:

    curr = root
    queue = deque([root])
    result = []

    while(queue):

        levels = len(queue)
        
        for i in range(levels):

            curr = queue.popleft()

            if(i == 0):
                result.append(curr.data)

            if(curr.left):
                queue.append(curr.left)
            elif(curr.right):
                queue.append(curr.right)

    return result