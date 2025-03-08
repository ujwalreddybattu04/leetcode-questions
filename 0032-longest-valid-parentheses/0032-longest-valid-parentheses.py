class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize stack with -1 to handle edge cases
        max_length = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push index of '('
            else:
                stack.pop()  # Pop the last '(' or previous unmatched index
                if stack:
                    max_length = max(max_length, i - stack[-1])  # Update max length
                else:
                    stack.append(i)  # Push current index as new unmatched ')'

        return max_length
