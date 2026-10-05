class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = {}
        left = 0
        result = 0

        for right, val in enumerate(s):
            if val in charDict and charDict[val] >= left:
                left = charDict[val] + 1
            charDict[val] = right
            result = max(result, right - left + 1)
        return result