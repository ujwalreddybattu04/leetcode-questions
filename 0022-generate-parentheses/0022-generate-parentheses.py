class Solution:
    def generateParenthesis(self, n: int):
        result = []
        
        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:  # Base case: valid combination found
                result.append(current)
                return
            
            if open_count < n:  # Add '(' if we haven't used all '('
                backtrack(current + "(", open_count + 1, close_count)
            
            if close_count < open_count:  # Add ')' if it can be closed properly
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)  # Start backtracking
        return result

# Example Usage:
solution = Solution()
print(solution.generateParenthesis(3))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
print(solution.generateParenthesis(1))  # Output: ["()"]
