class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = "1"
        
        for _ in range(n - 1):
            count = 1
            curr = ""
            
            for i in range(1, len(prev)):
                if prev[i] == prev[i - 1]:
                    count += 1
                else:
                    curr += str(count) + prev[i - 1]
                    count = 1
            
            curr += str(count) + prev[-1]  # Add last group
            prev = curr  # Move to next iteration
            
        return prev

        