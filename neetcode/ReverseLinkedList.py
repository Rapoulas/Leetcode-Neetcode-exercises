
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    
    newHead = head
    if head.next:
        newHead = reverseList(head.next)
        head.next.next = head
    head.next = None

    return newHead

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)

b = reverseList(a)

while b:
    print(b.val)
    b = b.next