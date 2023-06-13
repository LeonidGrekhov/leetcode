'''
9. Palindrome Number

Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False  # Negative numbers and numbers ending in 0 are not palindromes

        reversed_x = 0
        while x > reversed_x:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10

        # For even-length palindromes, x and reversed_x will be equal
        # For odd-length palindromes, x will be one digit ahead of reversed_x
        return x == reversed_x or x == reversed_x // 10

s1 = Solution()
print(s1.isPalindrome(x = -121))