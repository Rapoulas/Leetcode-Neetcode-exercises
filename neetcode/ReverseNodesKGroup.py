
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    group = 0
    while cur and group < k:
        cur = cur.next
        group += 1

    if group == k:
        cur = self.reverseKGroup(cur, k)
        while group > 0:
            tmp = head.next
            head.next = cur
            cur = head
            head = tmp
            group -= 1
        head = cur
    return head

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)

b = reverseList(a)

while b:
    print(b.val)
    b = b.next