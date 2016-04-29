'''
recursive method
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1: 
            return [nums]
        
        rst = []
        for i in range(len(nums)):
            s = nums[:i] + nums[i+1:]  
            p = self.permute(s)  
            for x in p:  
                rst.append(nums[i:i+1] + x)  
        return rst 
