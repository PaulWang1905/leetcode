class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rst = [[]]
        for num in nums:
            ans = []
            for l in rst:
                for i in xrange(len(l) + 1):
                    ans.append(l[:i] + [num] + l[i:])
                    if i < len(l) and l[i] == num:
                        break
            rst = ans
        return ans
