from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists or len(lists) == 0:
            return None
        
    while len(lists) > 1:
        temp = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if i + 1 < len(lists) else None
            temp.append(merge_lists(l1, l2))
        lists = temp
    
    return lists[0]
    
def merge_lists(l1, l2):
    node = ListNode()
    ans = node
    
    while l1 and l2:
        if l1.val > l2.val:
            node.next = l2
            l2 = l2.next
        else:
            node.next = l1
            l1 = l1.next
        node = node.next
    
    if l1:
        node.next = l1
    else:
        node.next = l2
    
    return ans.next


list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)

a = mergeKLists([list1, list2, list3])
b = []
while a:
    b.append(a.val)
    a = a.next
print(b)