'''
Dynamic Planning
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(res, [], sorted(candidates), target)
        return res

    def dfs(self, res, path, candidates, target):
        if target < candidates[0]:
            return 
        for i in range(len(candidates)-1, -1, -1):
            if candidates[i] == target:
                res.insert(0, [candidates[i]] + path)
            
            elif candidates[i] < target:
                self.dfs(res, [candidates[i]] + path, candidates[:i+1], target - candidates[i])
