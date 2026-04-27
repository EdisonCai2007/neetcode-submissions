class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        lp, rp = 0, 1
        max_len = 1
        freq = {s[0]}

        while rp < len(s):
            if s[rp] not in freq:
                # substring can be longer
                freq.add(s[rp])
                max_len = max(max_len, len(freq))
                rp += 1
            else:
                # duplicate found
                while s[lp] != s[rp]:
                    freq.remove(s[lp])
                    lp += 1
                lp += 1
                rp += 1
                
                
        
        return max_len

    # d v d d f
    #       L
    #         R
    # {d}