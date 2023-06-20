''''
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordlist = s.split()
        if wordlist:
            return len(wordlist[-1])
        return 0
    def lengthOfLastWordWithPtr(self, s: str) -> int:
        i, length = len(s) - 1, 0
        while s[i] == " ": #loop through extra spaces in the back of the string
            i -= 1
        while i >= 0 and s[i] != " ": # count the characters that are not a space
            length += 1
            i -= 1
        return length
    
s1 = Solution()
print(s1.lengthOfLastWord(s="   fly me   to   the moon  "))
print(s1.lengthOfLastWordWithPtr(s="   fly me   to   the moon  "))