class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols

        left, right = 0, total - 1

        while left <= right:
            middle = (left + right) // 2
            row = middle // cols
            col = middle % cols
            if matrix[row][col] < target:
                left = middle + 1
            elif matrix[row][col] > target:
                right = middle - 1
            else:
                return True
        return False