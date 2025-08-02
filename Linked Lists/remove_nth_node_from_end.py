class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #(0)[1,2,3,4], n=2
    # s    f
    
    fast = head
    dummy = ListNode(0, head)
    slow = dummy
    for _ in range(n):
        fast = fast.next

    while(fast):
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next