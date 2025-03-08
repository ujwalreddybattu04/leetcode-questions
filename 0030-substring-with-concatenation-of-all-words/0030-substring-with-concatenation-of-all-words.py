from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        substr_len = word_len * num_words
        word_count = Counter(words)
        result = []

        for i in range(word_len):  # Shift start index within word length
            left = i  # Left pointer of the window
            right = i  # Right pointer of the window
            seen = {}

            while right + word_len <= len(s):
                word = s[right:right + word_len]  # Extract word
                right += word_len  # Move right pointer

                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1

                    while seen[word] > word_count[word]:  # Shrink window if too many of `word`
                        seen[s[left:left + word_len]] -= 1
                        left += word_len

                    if right - left == substr_len:  # Valid concatenated substring found
                        result.append(left)
                else:
                    seen.clear()  # Reset and move left
                    left = right

        return result
