'''
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for character in s:
            if character.isalnum():
                newStr += character.lower()
        return newStr == newStr[::-1]
    
    def isPalindromePtr(self, s: str) -> bool:
        s = re.sub(r'\W+', '', s) # s = re.sub(r'[^a-zA-Z0-9]', '', s)
        left, right = 0, len(s) - 1
        s = s.upper()
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
 

s1 = Solution()
print(s1.isPalindrome(s = "A man, a plan, a canal: Panama"))
print(s1.isPalindrome(s = "A man, a plan, a canal: "))
print(s1.isPalindromePtr(s = "A man, a plan, a canal: Panama"))
print(s1.isPalindromePtr(s = "A man, a plan, a canal: "))