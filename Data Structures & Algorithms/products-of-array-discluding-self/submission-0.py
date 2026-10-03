class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        ans = [1] * nums_len
        prefix = 1
        suffix = 1

        for i in range(nums_len):
            ans[i] = prefix
            prefix *= nums[i]
        
        for i in range(nums_len - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        return ans 