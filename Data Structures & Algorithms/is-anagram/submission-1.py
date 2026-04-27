class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        tl = list(t)

        for char in s:
            if char in tl:
                tl.remove(char)
            else:
                return False
        
        return len(tl) == 0