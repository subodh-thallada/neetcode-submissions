class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1

        maxP = 0

        while r < len(prices):
            if prices[l]<prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l=r
            r+=1

        return maxP






        """lowest=prices[0]
        lowest_ind = 0
        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
                lowest_ind = i

        highest = prices[lowest_ind]
        highest_ind = lowest_ind
        for j in range(lowest_ind, len(prices)):
            if prices[j] > highest:
                highest = prices[j]
                highest_ind = j

        return highest-lowest"""
        
