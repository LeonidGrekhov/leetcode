'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" } 
        #make a key for each closing bracket to check if there is an existing opening bracket
        for character in s:
            if character in closeToOpen: # if the closing bracket is in the key
                if stack and stack[-1] == closeToOpen[character]: # if the bracket on the end of stack matches the key and stack not empty
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character) #append opening bracket
        return not stack
        #return true if stack is empty otherwise return false

s1 = Solution()
print(s1.isValid(s = "()([])"))