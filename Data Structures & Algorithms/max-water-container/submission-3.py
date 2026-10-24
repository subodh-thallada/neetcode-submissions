class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1

        height = 0
        maxH = 0

        while l!=r:
            height = (r-l)*min(heights[l],heights[r])
            if height>maxH:
                maxH = height
            
            if heights[r]>=heights[l]:
                l=l+1
            else:
                r=r-1

        return maxH