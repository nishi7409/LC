# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_num = 0
        second_num = 0

        current_1 = l1
        current_2 = l2

        list_1 = list()
        while current_1:
            list_1.append(current_1.val)
            current_1 = current_1.next
        counter = len(list_1)-1
        for number in reversed(list_1):
            first_num += int(number * int(str("1") + str('0'*counter)))
            counter -= 1

        list_2 = list()
        while current_2:
            list_2.append(current_2.val)
            current_2 = current_2.next
        counter = len(list_2)-1
        for number in reversed(list_2):
            second_num += int(number * int(str("1") + str('0'*counter)))
            counter -= 1

        value = list(str(first_num + second_num))
        result = ListNode(0)
        current = result

        for number in reversed(value):
            current.next = ListNode(int(number))
            current = current.next
            current.next = None
           
        return result.next


        
        