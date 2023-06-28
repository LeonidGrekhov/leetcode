'''
739. Daily Temperatures
Medium

Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to 
wait after the ith day to get a warmer temperature. If there is no future day 
for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures) #inicialized with 0 for results default value
        stack = []  # pair: [temp, index]
        for i, t in enumerate(temperatures): #i is the index t is the temperature
            while stack and t > stack[-1][0]: # check if the top of stack is greater than current temp
                stackTemp, stackIndex = stack.pop() #temp, index
                res[stackIndex] = i - stackIndex #calculate day difference 
            stack.append((t, i))

        return res
s1 = Solution()
print(s1.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))
