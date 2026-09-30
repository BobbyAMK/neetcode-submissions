class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for k in range(len(s)):
            count[s[k]] = count.get(s[k], 0) + 1
            count[t[k]] = count.get(t[k], 0) - 1
        
        for val in count.values():
            if val != 0:
                return False
        return True