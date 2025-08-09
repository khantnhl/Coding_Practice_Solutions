
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
    dummy = ListNode(0)
    curr = dummy
    carry = 0

    while(l1 or l2):
        cursum = carry

        if(l1):
            cursum += l1.val
            l1 = l1.next
        if(l2):
            cursum += l2.val
            l2 = l2.next
        
        # 10
        carry = cursum // 10
        cursum = cursum % 10

        node = ListNode(cursum)

        curr.next = node
        curr = curr.next

    
    if(carry):
        curr.next=ListNode(carry)
    return dummy.next