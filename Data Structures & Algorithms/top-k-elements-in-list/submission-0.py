from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # table of num and freq
        # max freq <= length of nums
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            freq[c].append(n)
        
        results = []
        # range(start, stop, step)
        for i in range(len(freq)- 1, 0, -1):
            for n in freq[i]:
                results.append(n)
                if len(results) == k:
                    return results