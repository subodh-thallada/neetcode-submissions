class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num1 = set(nums)

        if len(num1) != len(nums):
            return True

        return False
        