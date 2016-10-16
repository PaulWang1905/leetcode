class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        ordered = lambda x, y: sorted(matrix[i][j] for i in range(x) for j in range(y))
        return ordered(n, n)[k-1]
