class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sorted_stack = sorted(set(nums))
        nums[:len(sorted_stack)] = sorted_stack
        return len(sorted_stack)