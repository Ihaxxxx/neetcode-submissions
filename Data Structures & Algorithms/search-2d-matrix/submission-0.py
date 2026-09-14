class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom_row = len(matrix) - 1
        top_row = 0
        while top_row <= bottom_row:

            middle_row = (top_row + bottom_row) // 2

            if matrix[middle_row][0] <= target <= matrix[middle_row][-1]:
                left_col = 0
                right_col = len(matrix[0]) - 1

                while left_col <= right_col:

                    middle_col = (left_col + right_col) // 2

                    if matrix[middle_row][middle_col] == target:
                        return True
                    elif matrix[middle_row][middle_col] > target:
                        right_col = middle_col - 1
                    else:
                        left_col = middle_col + 1
                
                return False
            elif matrix[middle_row][0] > target:
                bottom_row = middle_row - 1
            else:
                top_row = top_row + 1
        
        return False