class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t={}

        for i in s:
            hash_s[i]=1+hash_s.get(i,0)
            
        for j in t:
            hash_t[j]=1+hash_t.get(j,0)

        if hash_s == hash_t:
            return True
        
        return False