class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort
        nums_dict = {}
        result = []

        # Add all the numbers from `numbers` into a dictionary, along with their occurrence counts.
        for n in nums:
            nums_dict[n] = nums_dict.get(n, 0) + 1

        # create new bucket
        bucket = [[] for _ in range(len(nums) + 1)]
        # add frequency of each n to bucket list
        for n, freq in nums_dict.items():
            bucket[freq].append(n)
        # create a loop in reverse, start at 0
        for i in range(len(bucket) -1 , 0 , -1):
            # append the value with most freq to result
            for j in bucket[i]:
                result.append(j)
                # stop when result's len = k
                if len(result) == k:
                    return result