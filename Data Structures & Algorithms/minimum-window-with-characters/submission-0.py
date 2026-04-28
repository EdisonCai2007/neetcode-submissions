class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, org = {}, {}

        for c in t: # create needed freq dict
            org[c] = org.get(c, 0) + 1
        
        have, need = 0, len(org)
        min_lp, min_rp, min_len = 0, 0, float("infinity")
        lp = 0

        for rp in range(len(s)): # iterate sliding right pointer
            c = s[rp]
            window[c] = window.get(c, 0) + 1

            if c in org and window[c] == org[c]:
                # condition is met
                have += 1 

            while have == need:
                # update resposne
                if (rp - lp + 1) < min_len:
                    min_lp, min_rp = lp, rp
                    min_len = rp - lp + 1

                # update lp
                window[s[lp]] -= 1
                if s[lp] in org and window[s[lp]] < org[s[lp]]:
                    have -= 1
                lp += 1
            
        return s[min_lp:min_rp+1] if min_len != float("infinity") else ""
            