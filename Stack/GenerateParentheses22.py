'''
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []
        self.backtrack(n, stack, res, 0, 0)
        return res
    
    def backtrack(self, n, stack, res, openNum, closedNum):
        if openNum == closedNum == n:
            res.append("".join(stack))
            return
        if openNum < n:
            stack.append("(")
            self.backtrack(n, stack, res, openNum + 1, closedNum)
            stack.pop()
        if closedNum < openNum:
            stack.append(")")
            self.backtrack(n, stack, res, openNum, closedNum + 1)
            stack.pop()

s1 = Solution()

print(s1.generateParenthesis(n=4))