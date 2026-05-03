class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create cars list and sort it by position
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars = sorted(cars, key=lambda x: x[0])

        stack = []
        # iterate backwards
        for i in range(len(cars)-1, -1, -1):
            pos, speed = cars[i]
            t = (target - pos) / speed

            # add car to stack if prev time is shorter
            if not stack or stack[-1] < t:
                stack.append(t)

        # return size of stack
        return len(stack)