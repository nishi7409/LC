class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = dict()

        for index, number in enumerate(nums):
            if target-number in history:
                return [history[target-number], index]
            history[number] = index
