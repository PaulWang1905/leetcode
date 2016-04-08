'''
binary search
'''

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #binary search
        low, high = 0, len(nums) - 1
        while high - low > 1:
            mid = (high + low) >> 1
            count = 0
            for k in nums:
                if mid < k <= high:
                    count += 1
            if count > high - mid:
                low = mid
            else:
                high = mid
        return high
