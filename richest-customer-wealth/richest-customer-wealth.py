class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for nums_list in accounts:
            richest = max(sum(nums_list), richest)
        return richest