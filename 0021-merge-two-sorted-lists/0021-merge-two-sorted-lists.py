# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 1
        if list1 is None and list2 is None:
            return list1
        headnode = None
        prevnode = None
        
        while (True):
            if list1 is None or list2 is None:
                break
            elif list1.val <= list2.val:
                if headnode is None:
                    headnode = ListNode(val=list1.val)
                    prevnode = headnode
                else:
                    newnode = ListNode(val=list1.val)
                    prevnode.next = newnode
                    prevnode= newnode
                list1 = list1.next
            else:
                if headnode is None:
                    headnode = ListNode(val=list2.val)
                    prevnode = headnode
                else:
                    newnode = ListNode(val=list2.val)
                    prevnode.next = newnode
                    prevnode= newnode
                list2 = list2.next
        if list1 is None:
            if headnode is None:
                headnode = list2
            else:
                prevnode.next = list2
        elif list2 is None:
            if headnode is None:
                headnode =list1
            else:
                prevnode.next = list1
        return headnode