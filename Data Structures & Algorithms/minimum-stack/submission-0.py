class MinStack:
    stack: list

    def __init__(self):
        self.stack = []
        self.min_index = []

    def push(self, val: int) -> None:
        # if the new value is less than the current min, change min_index to current index
        if (not self.min_index) or val < self.stack[self.min_index[-1]]:
            # new minimum found
            self.min_index.append(len(self.stack))
        else:
            self.min_index.append(self.min_index[-1])
        # Add to the stack
        self.stack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.min_index.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_index[-1]]
