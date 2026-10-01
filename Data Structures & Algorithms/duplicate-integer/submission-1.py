class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num1 = set()

        for i in nums:
            if i in num1:
                return True
            else:
                num1.add(i)

        return False
        