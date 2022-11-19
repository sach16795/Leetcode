# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        a = head
        b = head
        while True:
            a = a.next
            b = b.next.next if b.next is not None else None
            if a is None or b is None:
                return False
            elif a.next == b.next:
                return True
                
        