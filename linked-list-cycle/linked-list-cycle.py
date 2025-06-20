# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        previously_hit = list()

        while head:
            if head in previously_hit:
                return True
            previously_hit.append(head)
            head = head.next
        return False