# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from operator import itemgetter

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        # brute force:
        temp = list()
        head1 = list1
        head2 = list2
        while head1:
            temp.append((head1, head1.val))
            head1 = head1.next

        while head2:
            temp.append((head2, head2.val))
            head2 = head2.next

        sorted_temp = sorted(temp, key=itemgetter(1))
        if not sorted_temp:
            return None

        result_head = sorted_temp[0][0]
        current = result_head

        for node, _ in sorted_temp:
            current.next = node
            current = current.next
        
        current.next = None
        return result_head
        """
        
        result = ListNode()
        current = result

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        return result.next