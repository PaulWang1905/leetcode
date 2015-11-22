'''
method: from both sides to the middle
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        highest = height[0]
        index = 0
        
        for i in range(len(height)):
            if height[i] > highest:
                highest = height[i]
                index = i
        
        water = 0
        floor = height[0]
            
        for i in range(index):
            if floor >= height[i]:
                water += floor-height[i]
            else:
                floor = height[i]
        floor = 0    
        for i in range(len(height)-1, index, -1):
            if floor >= height[i]:
                water += floor-height[i]
            else:
                floor = height[i]
        return water
