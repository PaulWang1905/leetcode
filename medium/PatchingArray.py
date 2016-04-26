class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        rst = 1
        i = ans = 0
        while rst <= n:
            if i < len(nums) and rst >= nums[i]:
                rst += nums[i]
                i += 1
            else:
                rst += rst
                ans += 1
        return ans
