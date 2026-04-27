class Solution:
    def trap(self, height: List[int]) -> int:  
        final_area = 0
        max_height = max(height)

        for water_level in range(max_height, 0, -1):
            lp, rp = 0, len(height) - 1

            while height[lp] < water_level or height[rp] < water_level:
                if height[lp] < water_level:
                    lp += 1
                else:
                    rp -= 1

            area = max(rp - lp - 1, 0)
            rp -= 1

            while lp < rp:
                if height[rp] >= water_level:
                    area -= 1
                
                rp -= 1 

            final_area += area

        return final_area