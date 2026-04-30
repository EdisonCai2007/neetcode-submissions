class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # If numeric, add to the stack
            # If operator, perform operator on top 2 elements
            if token == '+': # Add
                stack.append(stack.pop() + stack.pop())
            elif token == '-': # Subtract
                num_2 = stack.pop()
                num_1 = stack.pop()
                stack.append(num_1 - num_2)
            elif token == '*': # Multiply
                stack.append(stack.pop() * stack.pop())
            elif token == '/': # Divide
                num_2 = stack.pop()
                num_1 = stack.pop()
                stack.append(math.trunc(num_1 / num_2))
            else:
                stack.append(int(token))

        # Return top of the stack
        return stack.pop()
        