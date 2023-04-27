class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False  # Negative numbers and numbers ending in 0 are not palindromes

        reversed_x = 0
        while x > reversed_x:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10

        # For even-length palindromes, x and reversed_x will be equal
        # For odd-length palindromes, x will be one digit ahead of reversed_x
        return x == reversed_x or x == reversed_x // 10