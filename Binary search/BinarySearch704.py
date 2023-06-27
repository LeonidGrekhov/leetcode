'''
704. Binary Search
Easy

Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 
Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1 #set pointers to both sides of the array
        while left <= right:
            mid = (left + right) // 2 # find the middle of the array
            if target < nums[mid]: # if taget is less than middle
                right = mid - 1
            elif target > nums[mid]: # if taget is greater than middle
                left = mid + 1 
            elif target == nums[mid]:                  
                return mid
        return -1

s1 = Solution()
print(s1.search(nums=[-1,0,3,5,9,12], target=13))