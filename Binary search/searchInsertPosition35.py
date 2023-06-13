'''
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104'''

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) #set pointers to both sides of the array
        while left < right:
            mid = (left + right) // 2 # find the middle of the array
            if target == nums[mid]: # if we get lucky and select the middle as the target we just return the position
                return mid
            if target > nums[mid]: # if taget is greater than middle
                left = mid + 1 
            else:                  # if taget is less than middle
                right = mid
        return left
s1 = Solution()
print(s1.searchInsert(nums=[1,2,5,7], target=6))