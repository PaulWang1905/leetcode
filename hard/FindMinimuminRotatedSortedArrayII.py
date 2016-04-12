'''
search the first corner
'''

class Solution(object):
	def findMin(self, nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	rst = nums[0]
	for i in range(len(nums) - 1):
		if nums[i] > nums[i+1]:
			rst = nums[i+1]
			break
	return rst
