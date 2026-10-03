class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # using set()

        nSet = set(nums)
        longest = 0

        for n in nSet:
            if (n-1) not in nSet:
                seqLength = 0
                while (n + seqLength) in nSet:
                    seqLength += 1
                longest = max(seqLength, longest)
        return longest