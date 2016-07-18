class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row, col = [], []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        row, col = set(row), set(col)
        for i in row:
            for j in range(n):
                matrix[i][j] = 0
        for i in range(m):
            for j in col:
                matrix[i][j] = 0
