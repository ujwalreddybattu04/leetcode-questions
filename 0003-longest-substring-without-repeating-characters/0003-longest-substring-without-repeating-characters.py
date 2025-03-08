class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:  # Remove characters from the left if duplicate found
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])  # Add current character to the set
            max_length = max(max_length, right - left + 1)  # Update max length

        return max_length
