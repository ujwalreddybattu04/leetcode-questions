class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # Remove leading whitespaces
        if not s:
            return 0
        
        sign, index = 1, 0
        if s[0] in "+-":  # Check for sign
            sign = -1 if s[0] == '-' else 1
            index += 1
        
        num = 0
        while index < len(s) and s[index].isdigit():
            num = num * 10 + int(s[index])
            index += 1
        
        num *= sign
        return max(-2**31, min(num, 2**31 - 1))  # Clamp to 32-bit integer range
