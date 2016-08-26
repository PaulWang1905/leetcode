class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ele in s:
            if ele in ['(','{','[']:
                stack.append(ele)
            else:
                if stack == []:
                    return False
                if stack[-1] == '(' and ele == ')' or stack[-1] == '{' and ele == '}' or stack[-1] == '[' and ele == ']':
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
