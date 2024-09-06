# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        prev = None
        node = head
        nums = set(nums)
        while node is not None:
            if node.val not in nums:
                if new_head == None:
                    new_head = ListNode(node.val, None)
                    prev = new_head
                    node = node.next
                    continue
                prev.next = ListNode(node.val, None)
                prev = prev.next
                node = node.next
            else:
                node = node.next
        return new_head