class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}
        
        for char in s:
            if char in s_count:
                s_count[char] += s_count.get(char, 0)
            s_count[char] = s_count.get(char, 0) + 1
        for char in t:
            if char in t_count:
                t_count[char] += t_count.get(char, 0)
            t_count[char] = t_count.get(char, 0) + 1

        all_keys = set(s_count.keys()) | set(t_count.keys())

        for k in all_keys:
            if s_count.get(k, 0) != t_count.get(k, 0):
                return False
        return True 