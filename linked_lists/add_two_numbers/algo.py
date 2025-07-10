from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def as_list(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result

    @classmethod
    def from_list(cls, lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    res = ListNode()

    c1, c2, c3 = l1, l2, res

    while c1 or c2:
        if c1:
            c3.val += c1.val
            c1 = c1.next
        if c2:
            c3.val += c2.val
            c2 = c2.next

        if c3.val >= 10:
            c3.val = c3.val - 10
            c3.next = ListNode(1) # carry 1

        if c1 or c2:
            if not c3.next:
                c3.next = ListNode()
            c3 = c3.next

    return res
