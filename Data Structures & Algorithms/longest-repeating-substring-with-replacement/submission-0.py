class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        
        freq = {s[0]: 1}

        lp, rp = 0, 1
        max_len = 1
        max_str = s[0]

        while rp < len(s):
            freq[s[rp]] = freq.get(s[rp], 0) + 1
            if freq[s[rp]] >= freq[max_str]:
                max_str = s[rp]
            
            if (rp - lp + 1) - freq[max_str] <= k:
                # string is valid
                max_len = max(max_len, rp - lp + 1)
                rp += 1
            else:
                freq[s[lp]] -= 1
                lp += 1
                rp += 1
        
        return max_len