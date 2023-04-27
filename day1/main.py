
import unittest
from twoSum import Solution
from isPalindrome import Solution2
from romanInt import Solution3



class TestSolutionTwoSum(unittest.TestCase):

        def test_1(self):
            nums = [2,7,11,15]
            target = 9
            result = Solution()
            self.assertEqual(result.twoSum(nums, target), [0, 1], "incorrect solution")
        def test_2(self):
            nums = [3, 2, 4]
            target = 6
            result = Solution()
            self.assertEqual(result.twoSum(nums, target), [1, 2], "incorrect solution")

        def test_3(self):
            nums = 121
            result = Solution2()
            self.assertEqual(result.isPalindrome(nums), True, "incorrect solution")
        
        def test_4(self):
            s = "III"
            result = Solution3()
            self.assertEqual(result.romanToInt(s), 3, "incorrect solution")
        def test_5(self):
            s = "LVIII"
            result = Solution3()
            self.assertEqual(result.romanToInt(s), 58, "incorrect solution")

unittest.main()