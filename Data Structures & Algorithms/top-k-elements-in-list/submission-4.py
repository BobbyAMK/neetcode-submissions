class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        result = []
        for n in nums:
            nums_dict[n] = nums_dict.get(n, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in nums_dict.items():
            buckets[freq].append(num)
        
        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                result.append(j)
                if len(result) == k:
                    return result