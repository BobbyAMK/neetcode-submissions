class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset = {}
        for idx, nums in enumerate(numbers, start=1):
            diff = target - nums
            if diff in hashset:
                return [hashset[diff], idx]
            hashset[nums] = idx