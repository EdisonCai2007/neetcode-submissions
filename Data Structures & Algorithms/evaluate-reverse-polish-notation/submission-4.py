class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', "/"}

        for token in tokens:
            # If numeric, add to the stack
            if token in operators:
                num_2 = stack.pop()
                num_1 = stack.pop()

                # If operator, perform operator on top 2 elements
                if token == '+': # Add
                    stack.append(num_1 + num_2)
                elif token == '-': # Subtract
                    stack.append(num_1 - num_2)
                elif token == '*': # Multiply
                    stack.append(num_1 * num_2)
                else: # Divide
                    stack.append(math.trunc(num_1 / num_2))
            else:
                stack.append(int(token))

        # Return top of the stack
        return stack.pop()
        