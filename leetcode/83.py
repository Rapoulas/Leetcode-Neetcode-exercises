
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = head
    while dummy and dummy.next:
        if dummy.val == dummy.next.val:
            dummy.next = dummy.next.next
        dummy = dummy.next
    return head

a = ListNode(1)
a.next = ListNode(1)
a.next.next = ListNode(1)
a.next.next.next = ListNode(1)

b = deleteDuplicates(a)
while b:
    #print(b.val)
    b = b.next