class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cSet = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in cSet:
                cSet.remove(s[left])
                left += 1
            cSet.add(s[right])
            result = max(result, right - left + 1)
        return result