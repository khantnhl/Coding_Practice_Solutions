"""
Summary: 
    use Hashmap and Doubly Linked List to handle priorities 
    
    get 
        - if key already exists 
        - remove and insert at right
    put 
        - if key already exists
        - remove 
        - create new Node
        - insert 
        - check capacity
"""
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left, self.right = ListNode(0,0), ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def get(self, key: int) -> int:
        if(key in self.cache):
            # remove and insert to maintain the order again
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # if key exists, remove
        # else create new Node and insert
        # check capacity and remove/del both from LinkedList and Hashmap if needed
        if(key in self.cache):
            self.remove(key)

        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if(len(self.cache) > self.cap):
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
    
    def remove(self, node : ListNode) -> int:
        prev = node.prev
        next = node.next

        prev.next = node
        next.prev = prev
    
    def insert(self, node : ListNode) -> int:
        prev = self.right.prev
        next = self.right
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)