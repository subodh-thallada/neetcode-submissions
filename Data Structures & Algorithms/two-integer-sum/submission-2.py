class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we need index and value
        prevMap = {}

        for i,n in enumerate(nums):
            if target-n not in prevMap:
                prevMap[n]=i
            else:
                return [prevMap[target-n],i]