class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                low, high= 0, len(matrix[0]) - 1
                while low <= high:
                    mid = (low + high) / 2
                    if target < matrix[i][mid]:
                        high = mid - 1
                    elif target > matrix[i][mid]:
                        low = mid + 1
                    else:
                        return True
        return False
