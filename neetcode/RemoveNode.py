from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -=1
    
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next

a = ListNode(1)
a.next = ListNode(2)

b = removeNthFromEnd(a, 2)

while b:
    print(b.val)
    b = b.next