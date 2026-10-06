class Solution:
    def trap(self, height: List[int]) -> int:
        amount = 0
        leftMax = rightMax = 0
        left, right = 0, len(height) - 1

        for _ in height:
            while left < right:
                if height[left] < height[right]:
                    leftMax = max(leftMax, height[left])
                    amount += leftMax - height[left]
                    left += 1
                else:
                    rightMax = max(rightMax, height[right])
                    amount += rightMax - height[right]
                    right -= 1
        return amount



            