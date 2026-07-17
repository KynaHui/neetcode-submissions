# time: O(n) -> scan through every element once
# space: O(n) -> stack
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "]": "[", "}": "{"} # hash map

        for c in s: 
            # close 
            if c in brackets:
                # stack not empty, top item in stack match
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
            else: # open 
                stack.append(c)

        # empty stack
        return True if not stack else False
