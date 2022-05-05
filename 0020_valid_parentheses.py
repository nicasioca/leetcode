class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        result = True
        
        for val in s:
            
            # if you have a False result return False immediately
            # if you let it run it reverts back to True like with ({{{{}}}))
            if result:
                if '(' == val or '{' == val or '[' == val:
                    stack.append(val)
                elif ')' == val:
                    result = len(stack) > 0 and stack.pop() == '('
                elif '}' == val:
                    result = len(stack) > 0 and stack.pop() == '{'
                elif ']' == val:
                    result = len(stack) > 0 and stack.pop() == '['
            else:
                return result
                
        # if you have True result but Stack not empty return False
        # stack would be not empty if appended multiple opens and only had one closed
        return result and len(stack) == 0
            

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false