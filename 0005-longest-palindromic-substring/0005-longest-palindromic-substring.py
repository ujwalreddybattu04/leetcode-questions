class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        start, max_length = 0, 0
        
        def expandAroundCenter(left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        
        for i in range(len(s)):
            l1, r1 = expandAroundCenter(i, i)   # Odd length palindrome
            l2, r2 = expandAroundCenter(i, i + 1)  # Even length palindrome
            
            if r1 - l1 > max_length:
                start, max_length = l1, r1 - l1
            if r2 - l2 > max_length:
                start, max_length = l2, r2 - l2
        
        return s[start: start + max_length + 1]

        

        