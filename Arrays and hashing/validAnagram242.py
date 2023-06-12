class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
    def isAnagramWithCounter(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    
s1 = Solution()
print(s1.isAnagram(s="anagram", t="nagaram"))
print(s1.isAnagramWithCounter(s="anagram", t="nagaram"))