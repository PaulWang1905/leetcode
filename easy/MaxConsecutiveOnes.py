class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        str_nums = ''.join(map(repr, nums))
        list_nums = str_nums.split('0')
        return max(map(len, list_nums))
