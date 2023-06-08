class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums))!=len(nums)
    def containsDuplicateHashSolution(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
s1 = Solution()
print(s1.containsDuplicate(nums=[1,2,3,1]))
print(s1.containsDuplicateHashSolution(nums=[1,2,3,1]))