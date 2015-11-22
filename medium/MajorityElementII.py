'''
method: 2 elements at most to meet demands
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums
            
        m = nums[0]
        n = 0
        x = 1
        y = 0
        
        for i in range(1, len(nums)):
            tmp = nums[i]
            if m == tmp:
                x += 1 
            elif n == tmp:
                y += 1
            elif x == 0:
                m = tmp
                x = 1
            elif y == 0:
                n = tmp
                y = 1
            else:
                x -= 1
                y -= 1
        
        x = 0
        y = 0
        for i in range(len(nums)):
            if nums[i] == m:
                x += 1
            elif nums[i] == n:
                y += 1
        
        res = []
        if x > len(nums)/3:
            res.append(m)
        if y > len(nums)/3:
            res.append(n)
            
        return res
