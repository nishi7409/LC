# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        # brute force
        temp = list()
        curr = head
        while curr:
            temp.append(curr.val)
            curr = curr.next
        middle_length = math.ceil(len(temp)/2)

        new_curr = head
        if len(temp)%2 != 0:
            for x in range(middle_length-1):
                new_curr = new_curr.next
        else:
            for x in range(middle_length):
                new_curr = new_curr.next
        return new_curr
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow