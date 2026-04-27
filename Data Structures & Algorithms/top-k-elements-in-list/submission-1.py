class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        freq_group = defaultdict(list)
        max_freq = 0

        for num in nums:
            freq[num] += 1

            if freq[num] > max_freq:
                max_freq += 1
                freq_group[max_freq] = []

            freq_group[freq[num]].append(num)

        res = set()
        for key in sorted(freq_group, reverse=True):
            for num in freq_group[key]:
                res.add(num)

                if len(res) >= k:
                    return list(res)

        return list(res)