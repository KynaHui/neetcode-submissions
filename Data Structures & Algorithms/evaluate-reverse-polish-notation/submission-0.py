# time: O(n), space: O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            elif i in operators and len(stack) >= 2:
                # first pop() is right operand
                num2, num1 = stack.pop(), stack.pop()
                if i == "+":
                    stack.append(num1 + num2)
                elif i == "-":
                    stack.append(num1 - num2)
                elif i == "*":
                    stack.append(num1 * num2)
                else:
                    # truncate towards 0: remove the decimal part and move toward 0.
                    stack.append(int(num1 / num2))
            else:
                continue
        return stack[-1]
