class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {')':'(', ']': '[', '}': '{'}

        for c in s:
            if c in mapping.values(): # c is an opening bracket
                stack.append(c)
            else: # c is a closing bracket
                if len(stack) == 0 or stack.pop() != mapping[c]:
                    # closing and opening brackets dont match
                    return False
        
        if len(stack) > 0:
            return False
        else:
            return True

