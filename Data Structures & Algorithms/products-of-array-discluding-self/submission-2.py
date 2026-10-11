class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre1=[]
        post1 = [1]*len(nums)
        total = [1]*len(nums)

        for i in range(len(nums)):
            if i!=0:
                pre1.append(nums[i]*pre1[i-1])
            else:
                pre1.append(nums[i])
            
        for i in range(len(nums)-1,-1,-1):
            if i!=len(nums)-1:
                post1[i]=nums[i]*post1[i+1]
            else:
                post1[i] = nums[i]

        for i in range(len(nums)):
            if i==0:
                total[i]=post1[i+1]
            elif i==len(nums)-1:
                total[i]=pre1[i-1]
            else:
                total[i]=pre1[i-1]*post1[i+1]

        return total
        