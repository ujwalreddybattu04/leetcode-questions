class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:  # If it's a closing bracket
                top_element = stack.pop() if stack else '#'  # Pop or use a dummy value
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)  # Push opening bracket onto stack

        return not stack  # Return True if stack is empty (valid parentheses)

# Example usage:
solution = Solution()
print(solution.isValid("()"))        # True
print(solution.isValid("()[]{}"))    # True
print(solution.isValid("(]"))        # False


        