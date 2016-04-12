'''
two-way analysis
'''

class Solution(object):
	def canCompleteCircuit(self, gas, cost):
	"""
	:type gas: List[int]
	:type cost: List[int]
	:rtype: int
	"""
	if sum(cost) > sum(gas):
		return -1
		    
	start = save = 0
	for i in range(len(gas)):
		if gas[i] + save < cost[i]:
			start = i + 1
		else:
			save += gas[i] - cost[i]
	return start
