class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in hashset:
                return [hashset[diff], idx]
            hashset[n] = idx