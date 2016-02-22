'''
binary number
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return [[nums[x] for x in range(len(nums)) if i>>x&1] for i in range(2**len(nums))]
