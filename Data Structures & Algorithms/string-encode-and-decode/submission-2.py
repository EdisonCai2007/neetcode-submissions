class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstr = ''
        countstr = ''
        for string in strs:
            encodedstr += string
            countstr += str(len(string)) + ' '

        return encodedstr + '/#&' + countstr

    def decode(self, s: str) -> List[str]:
        res = []
        encodedstr, countstr = s.split('/#&')
        
        l = 0
        for num in countstr.split():
            res.append(encodedstr[l:l+int(num)])

            l += int(num)

        return res