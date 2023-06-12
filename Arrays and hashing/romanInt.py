class Solution3:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev_value = 0
        result = 0
        for c in s:
            value = roman_dict[c]
            if value > prev_value:
                result -= prev_value
            else:
                result += prev_value
            prev_value = value
        result += prev_value
        return result