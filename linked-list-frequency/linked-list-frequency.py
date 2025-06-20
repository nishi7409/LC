# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        data = dict()

        current = head

        while current:
            if current.val in data:
                data[current.val] += 1
            else:
                data[current.val] = 1
            current = current.next
        
        result = ListNode()
        current = result

        for _,v in data.items():
            current.next = ListNode(v)
            current = current.next

        return result.next            