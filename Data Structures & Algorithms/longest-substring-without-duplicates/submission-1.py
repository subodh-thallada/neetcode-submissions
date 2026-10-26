class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        final = set()
        maxL=0
        l=0

        for r in range(len(s)):
            while s[r] in final:
                final.remove(s[l])
                l+=1
            final.add(s[r])
            maxL=max(maxL,len(final))
        
        return maxL