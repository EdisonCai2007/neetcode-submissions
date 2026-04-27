class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum_area = 0 

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                area = min(heights[i], heights[j]) * (j-i)
                if area > maximum_area:
                    maximum_area = area
        
        return maximum_area