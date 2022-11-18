# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if head is None:
            return head
        evalnode = prev.next
        prev.next = None
        while evalnode:
            if prev.val == evalnode.val:
                evalnode = evalnode.next
            else:
                prev.next = evalnode
                prev = evalnode
                evalnode = evalnode.next
                prev.next = None
        return head
            