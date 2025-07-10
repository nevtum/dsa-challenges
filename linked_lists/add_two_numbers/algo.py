from typing import Optional
from operator import ne


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
        summ = 0
        if c1:
            summ += c1.val
            c1 = c1.next
        if c2:
            summ += c2.val
            c2 = c2.next

        if summ >= 10:
            c3.val = max(0, summ - 10)
            c3.next = ListNode()
        else:
            c3.val = summ

        if c1 or c2:
            c3.next = ListNode()
            c3 = c3.next

    return res
