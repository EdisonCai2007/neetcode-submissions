class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # create stack and index
        stack = [] # holds tuple: [temp, index]
        res = [0] * len(temperatures)

        # loop through all temperatures i
        for i in range(len(temperatures)):
            # while stack not empty and top is less than current
            while stack and stack[-1][0] < temperatures[i]: # warmer temp day found
                top_index = stack.pop()[1]
                res[top_index] = i - top_index # calculates days until current
   
            # add temperature to stack
            stack.append((temperatures[i], i))
        
        return res