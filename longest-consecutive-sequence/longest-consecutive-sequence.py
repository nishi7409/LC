class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_Set = set(nums)
        length = 0

        for num in num_Set:
            if num-1 not in num_Set:
                temp = 1
                while num+temp in num_Set:
                    temp += 1
                length = max(length, temp)
        return length