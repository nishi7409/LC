# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        # brute force
        previously_hit = list()

        while head:
            if head in previously_hit:
                return True
            previously_hit.append(head)
            head = head.next
        return False
        """

        """
        # this will only work if pos is the first index
        if not head:
            return False

        previous = head
        current = previous.next
        first_run = False

        while current:
            if previous.next == current and not first_run:
                current = current.next
                first_run = True
                continue
            if previous.next == current and first_run:
                return True
            current = current.next
        return False
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False




