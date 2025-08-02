"""
time : O(v + e)
space: O(v)
"""
class Node:
    def __init__(self,val=0,neighbors=None):
        self.val=val
        self.neighbors=[] if(neighbors) else None

def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    _cloneMap = {}
    # node : clone
    def recurClone(node):
        if(not node):
            return None

        if(node in _cloneMap):
            return _cloneMap[node]
        
        # create new node
        clone = Node(node.val)
        _cloneMap[node] = clone

        for neighbor in node.neighbors:
            clone.neighbors.append(recurClone(neighbor))

        return clone
    return recurClone(node)