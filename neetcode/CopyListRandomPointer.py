from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    map = {}
    if head is None:
        return None
    if head in map:
        return map[head]

    copy = Node(head.val)
    map[head] = copy
    copy.next = copyRandomList(head.next)
    copy.random = map.get(head.random)
    return copy