'''
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
from sortedcollections import OrderedSet
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = OrderedSet()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            result = max(result, right - left + 1)
        return result
    
s1 = Solution()
print(s1.lengthOfLongestSubstring(s="abcabcbb"))
print(s1.lengthOfLongestSubstring(s="bbbbb"))
print(s1.lengthOfLongestSubstring(s="pwwkew"))
