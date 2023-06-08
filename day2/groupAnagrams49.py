class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic={}
        for word in strs:
            sorted_word="".join(sorted(word))
            if sorted_word not in dic:
                dic[sorted_word]=[word]
            else:
                dic[sorted_word].append(word)
        return dic.values()

s1 =Solution()
print(s1.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
