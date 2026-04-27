class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        org = [0]*26

        for s in s1:
            org[ord(s) - 97] += 1

        lp, rp = 0, 0
        new = [0]*26

        for i in range(len(s1) - 1):
            new[ord(s2[rp]) - 97] += 1
            rp += 1

        while rp < len(s2):
            new[ord(s2[rp]) - 97] += 1
            if org == new:
                return True
            
            new[ord(s2[lp]) - 97] -= 1
            lp += 1
            rp += 1
        
        return False

            