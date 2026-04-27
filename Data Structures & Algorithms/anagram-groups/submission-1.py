class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        res = []

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in anagrams:
                anagrams[sorted_word] = []

            anagrams[sorted_word].append(word)
        
        for key in anagrams:
            res.append(anagrams[key])
        
        return res
