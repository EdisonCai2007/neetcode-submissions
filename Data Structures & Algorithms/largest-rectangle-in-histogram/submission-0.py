class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [height, pos]
        max_area = 0

        # iterate through all items in the list
        for i in range(len(heights)):
            # while prev item is greater than the current, calculate the area
            pos = i
            while stack and stack[-1][0] > heights[i]:
                height, pos = stack.pop()
                max_area = max(max_area, height * (i - pos))

            # add current to the stack, with pos at the prev item's pos
            stack.append([heights[i], pos])

        # calculate all extra areas
        while stack:
            height, pos = stack.pop()
            max_area = max(max_area, height * (len(heights) - pos))

        # return max
        return max_area

# #
# #
# #
# #  #
# #  #
# ####
######