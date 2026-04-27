class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s) - 1

        s.lower()
        while lp < rp:
            if s[lp].isalpha() or s[lp].isnumeric():
                if s[rp].isalpha() or s[rp].isnumeric():
                    if s[lp].lower() == s[rp].lower():
                        lp += 1
                        rp -= 1
                    else:
                        return False
                else:
                    rp -= 1
            else:
                lp += 1
        
        return True